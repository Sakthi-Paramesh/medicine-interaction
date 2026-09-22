import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from medsafety_app.models import Medicine

def seed_data():
    medicines = [
        {
            "medicine_name": "Paracetamol 500mg",
            "generic_name": "Acetaminophen",
            "brand_name": "Tylenol, Panadol, Calpol",
            "category": "Pain Relievers",
            "uses": "Used to treat mild to moderate pain (from headaches, menstrual periods, toothaches, backaches, osteoarthritis, or cold/flu aches and pains) and to reduce fever.",
            "symptoms": "Fever, Headache, Body pain",
            "dosage": "Adults: 1-2 tablets every 4-6 hours. Maximum 4000mg per day.",
            "side_effects": "Nausea, stomach pain, loss of appetite, itching, rash.",
            "common_side_effects": "Nausea, vomiting",
            "serious_side_effects": "Liver damage (if overdosed), allergic reactions",
            "food_to_eat": "Take with or without food. Avoid fasting while on high doses.",
            "food_to_avoid": "No specific food restrictions.",
            "alcohol_warning": "Avoid alcohol. Combining alcohol with Paracetamol increases the risk of severe liver damage.",
            "pregnancy_safety": "Generally considered safe during pregnancy if used as directed for short periods.",
            "breastfeeding_safety": "Safe to use while breastfeeding. Very small amounts pass into breast milk.",
            "kidney_warning": "Use with caution if you have severe kidney disease.",
            "liver_warning": "HIGH RISK. Do not use if you have severe liver disease. Overdose can cause fatal liver damage.",
            "drug_interactions": "Warfarin (blood thinner), Carbamazepine, Ketoconazole.",
            "prescription_required": False,
            "description": "Paracetamol is a widely used over-the-counter medication for pain and fever."
        },
        {
            "medicine_name": "Amoxicillin 250mg",
            "generic_name": "Amoxicillin",
            "brand_name": "Amoxil, Moxatag",
            "category": "Antibiotics",
            "uses": "Used to treat a wide variety of bacterial infections, such as ear infections, throat infections, pneumonia, and skin infections.",
            "symptoms": "Bacterial infections, Sore throat, Cough with phlegm",
            "dosage": "Varies by infection. Typically 250mg to 500mg every 8 hours.",
            "side_effects": "Nausea, vomiting, diarrhea, skin rash.",
            "common_side_effects": "Diarrhea, stomach upset",
            "serious_side_effects": "Severe allergic reactions (anaphylaxis), severe watery diarrhea (C. diff infection).",
            "alcohol_warning": "Alcohol does not directly interact, but it can worsen side effects like stomach upset and dizziness.",
            "pregnancy_safety": "Considered safe during pregnancy (Pregnancy Category B).",
            "breastfeeding_safety": "Generally safe, but may cause mild diarrhea in the nursing infant.",
            "allergy_warnings": "Do not take if you are allergic to penicillin or cephalosporin antibiotics.",
            "prescription_required": True,
            "description": "Amoxicillin is a penicillin antibiotic used to treat bacterial infections."
        },
        {
            "medicine_name": "Cetirizine 10mg",
            "generic_name": "Cetirizine Hydrochloride",
            "brand_name": "Zyrtec, Reactine",
            "category": "Respiratory",
            "uses": "Used to temporarily relieve allergy symptoms such as watery eyes, runny nose, sneezing, and itching.",
            "symptoms": "Runny nose, sneezing, itchy eyes, hives",
            "dosage": "Adults: 1 tablet (10mg) once daily.",
            "side_effects": "Drowsiness, dry mouth, tiredness.",
            "common_side_effects": "Drowsiness, fatigue, dry mouth",
            "serious_side_effects": "Difficulty breathing, severe dizziness.",
            "alcohol_warning": "Avoid alcohol. Alcohol can increase drowsiness and dizziness caused by cetirizine.",
            "driving_warning": "May cause drowsiness. Be careful driving or operating machinery until you know how it affects you.",
            "prescription_required": False,
            "description": "Cetirizine is a popular non-drowsy (though it can cause drowsiness in some) antihistamine for allergies."
        },
        {
            "medicine_name": "Pantoprazole 40mg",
            "generic_name": "Pantoprazole Sodium",
            "brand_name": "Protonix, Pantocid",
            "category": "Antacid",
            "uses": "Used to treat certain stomach and esophagus problems (such as acid reflux, ulcers). It works by decreasing the amount of acid your stomach makes.",
            "symptoms": "Heartburn, Acid reflux, Stomach ulcers",
            "dosage": "Usually 40mg once daily before a meal (preferably in the morning).",
            "side_effects": "Headache, diarrhea, stomach pain, gas.",
            "food_to_eat": "Best taken 30 minutes before a meal.",
            "kidney_warning": "May increase risk of certain kidney problems if used long-term.",
            "prescription_required": True,
            "description": "Pantoprazole reduces stomach acid and helps heal acid damage to the stomach and esophagus."
        },
        {
            "medicine_name": "Metformin 500mg",
            "generic_name": "Metformin Hydrochloride",
            "brand_name": "Glucophage, Glycomet",
            "category": "Anti-diabetic",
            "uses": "Used with a proper diet and exercise program and possibly with other medications to control high blood sugar in people with type 2 diabetes.",
            "symptoms": "High blood sugar, Type 2 Diabetes",
            "dosage": "Starts with 500mg once or twice a day with meals.",
            "side_effects": "Nausea, vomiting, stomach upset, diarrhea, metallic taste in the mouth.",
            "food_to_eat": "Take with meals to reduce stomach upset.",
            "alcohol_warning": "Avoid heavy alcohol use. Combining heavy alcohol use with metformin increases the risk of lactic acidosis.",
            "kidney_warning": "Not recommended for patients with severe kidney disease.",
            "liver_warning": "Use with caution; liver disease increases the risk of lactic acidosis.",
            "prescription_required": True,
            "description": "Metformin is a first-line medication for the treatment of type 2 diabetes."
        },
        {
            "medicine_name": "Aspirin 75mg",
            "generic_name": "Acetylsalicylic acid",
            "brand_name": "Ecosprin, Bayer Aspirin",
            "category": "Cardiology",
            "uses": "Used to prevent blood clots, reducing the risk of stroke and heart attack.",
            "symptoms": "Heart disease risk, blood clots",
            "dosage": "Usually 75mg - 150mg once daily as directed by doctor.",
            "side_effects": "Stomach upset, heartburn, easy bruising.",
            "common_side_effects": "Stomach pain, heartburn",
            "serious_side_effects": "Severe bleeding, black stools, ringing in ears.",
            "food_to_eat": "Take with food or a full glass of water to avoid stomach upset.",
            "alcohol_warning": "Avoid heavy alcohol use, as it increases the risk of stomach bleeding.",
            "prescription_required": True,
            "description": "Low-dose aspirin is commonly used as a blood thinner for cardiology patients."
        }
    ]

    print("Clearing old medicine data...")
    Medicine.objects.all().delete()
    
    print(f"Adding {len(medicines)} medicines to the database...")
    for data in medicines:
        Medicine.objects.create(**data)
        print(f" - Added {data['medicine_name']}")
        
    print("Database seeding completed successfully!")

if __name__ == '__main__':
    seed_data()
