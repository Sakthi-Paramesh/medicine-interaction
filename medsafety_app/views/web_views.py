from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Medicine
from ..services.ai_service import generate_medicine_info

def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'login.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'register.html')

@login_required(login_url='login')
def dashboard(request):
    context = {
        'username': request.user.username,
        'isAdmin': request.user.role == 'ADMIN'
    }
    if context['isAdmin']:
        return render(request, 'admin_dashboard.html', context)
    return render(request, 'user_dashboard.html', context)

@login_required(login_url='login')
def saved_medicines_page(request):
    return render(request, 'saved_medicines.html')

def search_page(request):
    return render(request, 'search.html')

def scanner_page(request):
    return render(request, 'prescription_scanner.html')

def interaction_page(request):
    return render(request, 'interaction.html')

def medicine_detail_page(request, id):
    # This was a dynamic fetch in java, it just passes the ID.
    context = {'medicineId': id}
    return render(request, 'medicine_detail.html', context)

def medicine_ai_detail_page(request):
    query = request.GET.get('q', '')
    
    # Generate medicine info via AI service
    med_info = generate_medicine_info(query)
    
    # Render with context
    context = {
        'medicine': med_info,
        'isAiGenerated': True,
        'query': query
    }
    return render(request, 'medicine_ai_detail.html', context)
