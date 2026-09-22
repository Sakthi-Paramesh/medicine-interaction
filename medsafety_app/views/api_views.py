import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from ..models import User, Medicine, SavedMedicine, SearchHistory
from ..services.ai_service import check_interactions, answer_follow_up_question, analyze_prescription
from ..services.ocr_service import extract_text_from_image

@csrf_exempt
@require_POST
def login_api(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return JsonResponse({'message': 'Logged in successfully', 'token': 'session-based'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

@csrf_exempt
@require_POST
def register_api(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email', '')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username already exists'}, status=400)
            
        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'message': 'User registered successfully'})
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

@csrf_exempt
@require_POST
def logout_api(request):
    django_logout(request)
    return JsonResponse({'message': 'Logged out successfully'})


def search_medicine_api(request):
    query = request.GET.get('query', request.GET.get('q', '')).strip()
    if not query:
        return JsonResponse([], safe=False)
    
    medicines = Medicine.objects.filter(medicine_name__icontains=query)
    results = [{'id': m.id, 'medicineName': m.medicine_name, 'genericName': m.generic_name, 'category': m.category} for m in medicines]
    return JsonResponse(results, safe=False)

def get_medicine_api(request, id):
    try:
        m = Medicine.objects.get(id=id)
        # Serialize fields. Doing it simply here:
        data = {
            'id': m.id,
            'medicineName': m.medicine_name,
            'genericName': m.generic_name,
            'brandName': m.brand_name,
            'imageUrl': m.image_url,
            'category': m.category,
            'uses': m.uses,
            'symptoms': m.symptoms,
            'dosage': m.dosage,
            'sideEffects': m.side_effects,
            'commonSideEffects': m.common_side_effects,
            'seriousSideEffects': m.serious_side_effects,
            'foodToEat': m.food_to_eat,
            'foodToAvoid': m.food_to_avoid,
            'alcoholWarning': m.alcohol_warning,
            'pregnancySafety': m.pregnancy_safety,
            'breastfeedingSafety': m.breastfeeding_safety,
            'kidneyWarning': m.kidney_warning,
            'liverWarning': m.liver_warning,
            'childrenSafety': m.children_safety,
            'elderlySafety': m.elderly_safety,
            'drivingWarning': m.driving_warning,
            'drugInteractions': m.drug_interactions,
            'diseaseInteractions': m.disease_interactions,
            'allergyWarnings': m.allergy_warnings,
            'storageInstructions': m.storage_instructions,
            'missedDoseInstructions': m.missed_dose_instructions,
            'overdoseInformation': m.overdose_information,
            'alternativeMedicines': m.alternative_medicines,
            'similarMedicines': m.similar_medicines,
            'prescriptionRequired': m.prescription_required,
            'manufacturer': m.manufacturer,
            'description': m.description,
            'faqs': m.faqs,
            'medicalDisclaimer': m.medical_disclaimer,
        }
        return JsonResponse(data)
    except Medicine.DoesNotExist:
        return JsonResponse({'message': 'Medicine not found'}, status=404)

@csrf_exempt
@require_POST
def save_medicine_api(request, medicine_id):
    if not request.user.is_authenticated:
        return JsonResponse({'message': 'Unauthorized'}, status=401)
        
    try:
        medicine = Medicine.objects.get(id=medicine_id)
        SavedMedicine.objects.get_or_create(user=request.user, medicine=medicine)
        return JsonResponse({'message': 'Medicine saved successfully', 'saved': True})
    except Medicine.DoesNotExist:
        return JsonResponse({'message': 'Medicine not found'}, status=404)

@csrf_exempt
def unsave_medicine_api(request, medicine_id):
    if request.method == 'DELETE' or request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'Unauthorized'}, status=401)
            
        try:
            medicine = Medicine.objects.get(id=medicine_id)
            SavedMedicine.objects.filter(user=request.user, medicine=medicine).delete()
            return JsonResponse({'message': 'Medicine removed from saved list', 'saved': False})
        except Medicine.DoesNotExist:
            return JsonResponse({'message': 'Medicine not found'}, status=404)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@require_GET
def check_save_status_api(request, medicine_id):
    if not request.user.is_authenticated:
        return JsonResponse({'saved': False})
        
    try:
        medicine = Medicine.objects.get(id=medicine_id)
        exists = SavedMedicine.objects.filter(user=request.user, medicine=medicine).exists()
        return JsonResponse({'saved': exists})
    except Medicine.DoesNotExist:
        return JsonResponse({'saved': False})

@require_GET
def recent_searches_api(request):
    if not request.user.is_authenticated:
        return JsonResponse([], safe=False)
        
    # Get top 10 distinct
    history = SearchHistory.objects.filter(user=request.user).order_by('-searched_at')
    # Manual distinct to preserve order
    queries = []
    for h in history:
        if h.query not in queries:
            queries.append(h.query)
        if len(queries) == 10:
            break
    return JsonResponse(queries, safe=False)

@require_GET
def saved_medicines_api(request):
    if not request.user.is_authenticated:
        return JsonResponse([], safe=False)
        
    saved = SavedMedicine.objects.filter(user=request.user).order_by('-saved_at')
    # Only return fields needed for the card
    results = [{'id': s.medicine.id, 'medicineName': s.medicine.medicine_name, 'category': s.medicine.category} for s in saved]
    return JsonResponse(results, safe=False)

@csrf_exempt
@require_POST
def log_search_history_api(request):
    query = request.POST.get('query') or request.GET.get('query')
    if request.user.is_authenticated and query and query.strip():
        SearchHistory.objects.create(user=request.user, query=query.strip())
    return JsonResponse({'status': 'ok'})

@require_GET
def check_interaction_api(request):
    meds_param = request.GET.get('meds', '')
    if not meds_param:
        return JsonResponse({'analysis': 'No medicines provided.'})
        
    meds = [m.strip() for m in meds_param.split(',') if m.strip()]
    analysis = check_interactions(meds)
    return JsonResponse({'analysis': analysis})

@csrf_exempt
@require_POST
def scan_prescription_api(request):
    if 'file' not in request.FILES:
        return JsonResponse({'message': 'Please upload a file'}, status=400)
        
    file = request.FILES['file']
    try:
        extracted_text = extract_text_from_image(file)
        return JsonResponse({'text': extracted_text})
    except Exception as e:
        return JsonResponse({'message': f"Failed to process image: {str(e)}"}, status=500)
