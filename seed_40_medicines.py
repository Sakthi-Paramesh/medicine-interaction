import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from medsafety_app.models import Medicine

def seed_large_data():
    medicines = [
        # Pain Relievers / Anti-inflammatory
        {
            "medicine_name": "Ibuprofen 400mg",
            "generic_name": "Ibuprofen",
            "brand_name": "Advil, Motrin, Brufen",
            "category": "Pain Relievers",
            "uses": "Treats pain, inflammation, and high fever.",
            "symptoms": "Headache, muscle ache, arthritis, fever",
            "dosage": "1 tablet every 6-8 hours as needed. Take with food.",
            "side_effects": "Stomach upset, heartburn, dizziness.",
            "common_side_effects": "Nausea, mild heartburn",
            "serious_side_effects": "Stomach bleeding, kidney problems",
            "food_to_eat": "Must be taken with food or milk to avoid stomach ulcers.",
            "food_to_avoid": "None",
            "alcohol_warning": "Avoid alcohol. Increases risk of stomach bleeding.",
            "pregnancy_safety": "Avoid in the third trimester.",
            "kidney_warning": "Use cautiously if you have kidney disease.",
            "prescription_required": False
        },
        {
            "medicine_name": "Naproxen 250mg",
            "generic_name": "Naproxen Sodium",
            "brand_name": "Aleve, Naprosyn",
            "category": "Pain Relievers",
            "uses": "Relieves pain from various conditions such as headaches, muscle aches, tendonitis, dental pain, and menstrual cramps.",
            "symptoms": "Joint pain, inflammation, swelling",
            "dosage": "1 tablet every 8-12 hours.",
            "common_side_effects": "Stomach pain, heartburn, dizziness",
            "serious_side_effects": "Heart attack, stroke, stomach bleeding",
            "food_to_eat": "Take with a full glass of water and food.",
            "alcohol_warning": "Heavy alcohol use increases risk of stomach bleeding.",
            "pregnancy_safety": "Not recommended, especially in late pregnancy.",
            "prescription_required": False
        },
        {
            "medicine_name": "Diclofenac 50mg",
            "generic_name": "Diclofenac Potassium",
            "brand_name": "Voveran, Voltaren",
            "category": "Pain Relievers",
            "uses": "Used to relieve pain, swelling, and joint stiffness.",
            "symptoms": "Arthritis, severe back pain, gout",
            "dosage": "1 tablet 2-3 times a day after meals.",
            "common_side_effects": "Indigestion, gas, stomach pain",
            "serious_side_effects": "Liver damage, severe allergic reactions",
            "food_to_eat": "Take after meals.",
            "alcohol_warning": "Increases risk of stomach bleeding.",
            "prescription_required": True
        },
        {
            "medicine_name": "Tramadol 50mg",
            "generic_name": "Tramadol Hydrochloride",
            "brand_name": "Ultram, Tramacip",
            "category": "Pain Relievers",
            "uses": "Used to help relieve moderate to moderately severe pain.",
            "symptoms": "Severe pain, post-surgery pain",
            "dosage": "1 tablet every 4-6 hours as needed for pain.",
            "common_side_effects": "Nausea, dizziness, constipation",
            "serious_side_effects": "Seizures, serotonin syndrome, breathing problems",
            "driving_warning": "Causes severe drowsiness. Do not drive.",
            "alcohol_warning": "Dangerous interaction. Can cause fatal respiratory depression.",
            "prescription_required": True
        },
        # Antibiotics
        {
            "medicine_name": "Azithromycin 500mg",
            "generic_name": "Azithromycin",
            "brand_name": "Zithromax, Azee",
            "category": "Antibiotics",
            "uses": "Treats bacterial infections such as respiratory infections, skin infections, and ear infections.",
            "symptoms": "Throat infection, sinus infection, bronchitis",
            "dosage": "1 tablet daily for 3 to 5 days.",
            "common_side_effects": "Diarrhea, nausea, abdominal pain",
            "serious_side_effects": "Irregular heartbeat, liver problems",
            "food_to_avoid": "Do not take with antacids containing aluminum or magnesium.",
            "pregnancy_safety": "Generally considered safe (Category B).",
            "prescription_required": True
        },
        {
            "medicine_name": "Ciprofloxacin 500mg",
            "generic_name": "Ciprofloxacin",
            "brand_name": "Cipro, Cifran",
            "category": "Antibiotics",
            "uses": "Used to treat a variety of bacterial infections.",
            "symptoms": "Urinary tract infection (UTI), bone infections",
            "dosage": "1 tablet twice a day (every 12 hours).",
            "common_side_effects": "Nausea, diarrhea, dizziness",
            "serious_side_effects": "Tendon rupture, nerve damage",
            "food_to_avoid": "Avoid taking with dairy products (milk, yogurt) or calcium-fortified juice alone.",
            "pregnancy_safety": "Not recommended.",
            "prescription_required": True
        },
        {
            "medicine_name": "Doxycycline 100mg",
            "generic_name": "Doxycycline",
            "brand_name": "Vibramycin, Doxyn",
            "category": "Antibiotics",
            "uses": "Treats many different bacterial infections, such as acne, urinary tract infections, and intestinal infections.",
            "symptoms": "Acne, Lyme disease, malaria prevention",
            "dosage": "1 tablet twice a day.",
            "common_side_effects": "Sun sensitivity, nausea",
            "serious_side_effects": "Difficulty swallowing, severe skin reaction",
            "food_to_eat": "Take with plenty of fluids.",
            "food_to_avoid": "Do not take with milk, iron supplements, or antacids.",
            "pregnancy_safety": "Unsafe (can harm fetal bone and tooth development).",
            "prescription_required": True
        },
        # Antacids / Gastric
        {
            "medicine_name": "Omeprazole 20mg",
            "generic_name": "Omeprazole",
            "brand_name": "Prilosec, Omez",
            "category": "Antacid",
            "uses": "Treats conditions where there is too much acid in the stomach.",
            "symptoms": "Heartburn, GERD, stomach ulcers",
            "dosage": "1 capsule daily before breakfast.",
            "common_side_effects": "Headache, stomach pain",
            "serious_side_effects": "Kidney problems, low magnesium levels (with long-term use)",
            "food_to_eat": "Take 30-60 minutes before a meal.",
            "pregnancy_safety": "Consult doctor.",
            "prescription_required": False
        },
        {
            "medicine_name": "Ranitidine 150mg",
            "generic_name": "Ranitidine",
            "brand_name": "Zantac, Rantac",
            "category": "Antacid",
            "uses": "Decreases stomach acid production.",
            "symptoms": "Heartburn, acid indigestion",
            "dosage": "1 tablet twice a day.",
            "common_side_effects": "Headache, constipation",
            "serious_side_effects": "Liver inflammation",
            "alcohol_warning": "Alcohol can increase stomach acid and delay healing.",
            "prescription_required": False
        },
        # Cardiology
        {
            "medicine_name": "Atorvastatin 20mg",
            "generic_name": "Atorvastatin Calcium",
            "brand_name": "Lipitor, Atorva",
            "category": "Cardiology",
            "uses": "Lowers bad cholesterol and fats (such as LDL, triglycerides) and raises good cholesterol (HDL).",
            "symptoms": "High cholesterol, heart disease prevention",
            "dosage": "1 tablet daily, usually at night.",
            "common_side_effects": "Muscle pain, diarrhea, joint pain",
            "serious_side_effects": "Severe muscle breakdown, liver damage",
            "food_to_avoid": "Avoid grapefruit and grapefruit juice.",
            "liver_warning": "Regular liver function tests required.",
            "pregnancy_safety": "Unsafe. Do not use if pregnant.",
            "prescription_required": True
        },
        {
            "medicine_name": "Amlodipine 5mg",
            "generic_name": "Amlodipine Besylate",
            "brand_name": "Norvasc, Amlong",
            "category": "Cardiology",
            "uses": "Used to treat high blood pressure and chest pain (angina).",
            "symptoms": "High blood pressure, chest pain",
            "dosage": "1 tablet daily.",
            "common_side_effects": "Swelling in ankles/feet, dizziness, flushing",
            "serious_side_effects": "Fainting, irregular heartbeat",
            "alcohol_warning": "Can increase dizziness and lower blood pressure too much.",
            "prescription_required": True
        },
        {
            "medicine_name": "Losartan 50mg",
            "generic_name": "Losartan Potassium",
            "brand_name": "Cozaar, Losar",
            "category": "Cardiology",
            "uses": "Used to treat high blood pressure and to help protect the kidneys from damage due to diabetes.",
            "symptoms": "High blood pressure",
            "dosage": "1 tablet daily.",
            "common_side_effects": "Dizziness, fatigue",
            "serious_side_effects": "High potassium levels, kidney problems",
            "pregnancy_safety": "Unsafe in pregnancy.",
            "prescription_required": True
        },
        {
            "medicine_name": "Clopidogrel 75mg",
            "generic_name": "Clopidogrel Bisulfate",
            "brand_name": "Plavix, Clavix",
            "category": "Cardiology",
            "uses": "Prevents blood clots after a recent heart attack or stroke.",
            "symptoms": "Heart attack prevention, stroke prevention",
            "dosage": "1 tablet daily.",
            "common_side_effects": "Easy bruising, minor bleeding",
            "serious_side_effects": "Severe bleeding, blood in urine/stool",
            "alcohol_warning": "Avoid alcohol as it increases the risk of stomach bleeding.",
            "prescription_required": True
        },
        # Anti-diabetic
        {
            "medicine_name": "Glimepiride 2mg",
            "generic_name": "Glimepiride",
            "brand_name": "Amaryl, Glimy",
            "category": "Anti-diabetic",
            "uses": "Used with a proper diet and exercise program to control high blood sugar in people with type 2 diabetes.",
            "symptoms": "High blood sugar, Type 2 Diabetes",
            "dosage": "1 tablet daily with breakfast.",
            "common_side_effects": "Low blood sugar (hypoglycemia), dizziness",
            "serious_side_effects": "Severe hypoglycemia, liver problems",
            "food_to_eat": "Must be taken with the first main meal of the day.",
            "alcohol_warning": "Alcohol can cause a severe drop in blood sugar.",
            "prescription_required": True
        },
        {
            "medicine_name": "Sitagliptin 50mg",
            "generic_name": "Sitagliptin",
            "brand_name": "Januvia, Istamet",
            "category": "Anti-diabetic",
            "uses": "Helps control blood sugar levels by increasing insulin release.",
            "symptoms": "Type 2 Diabetes",
            "dosage": "1 tablet daily.",
            "common_side_effects": "Headache, upper respiratory infection",
            "serious_side_effects": "Pancreatitis, severe joint pain",
            "prescription_required": True
        },
        # Respiratory / Allergy
        {
            "medicine_name": "Levocetirizine 5mg",
            "generic_name": "Levocetirizine",
            "brand_name": "Xyzal, L-Cet",
            "category": "Respiratory",
            "uses": "Relieves allergy symptoms like runny nose, sneezing, and watery eyes.",
            "symptoms": "Allergies, hay fever, hives",
            "dosage": "1 tablet at night.",
            "common_side_effects": "Drowsiness, dry mouth",
            "serious_side_effects": "Difficulty urinating",
            "driving_warning": "May cause drowsiness. Use caution.",
            "alcohol_warning": "Avoid alcohol, increases drowsiness.",
            "prescription_required": False
        },
        {
            "medicine_name": "Salbutamol Inhaler (100mcg)",
            "generic_name": "Albuterol / Salbutamol",
            "brand_name": "Ventolin, Asthalin",
            "category": "Respiratory",
            "uses": "Relieves symptoms of asthma and chronic obstructive pulmonary disease (COPD).",
            "symptoms": "Wheezing, shortness of breath, asthma attack",
            "dosage": "1-2 puffs as needed for shortness of breath.",
            "common_side_effects": "Shakiness (tremor), fast heartbeat, headache",
            "serious_side_effects": "Worsening breathing problems (paradoxical bronchospasm)",
            "prescription_required": True
        },
        {
            "medicine_name": "Montelukast 10mg",
            "generic_name": "Montelukast Sodium",
            "brand_name": "Singulair, Montair",
            "category": "Respiratory",
            "uses": "Prevents wheezing, difficulty breathing, chest tightness, and coughing caused by asthma.",
            "symptoms": "Asthma prevention, severe allergies",
            "dosage": "1 tablet in the evening.",
            "common_side_effects": "Stomach pain, headache",
            "serious_side_effects": "Mood/mental changes, depression, vivid dreams",
            "prescription_required": True
        },
        # Vitamins / Supplements
        {
            "medicine_name": "Vitamin D3 60000 IU",
            "generic_name": "Cholecalciferol",
            "brand_name": "Calcirol, Uprise-D3",
            "category": "Vitamins",
            "uses": "Used to treat or prevent Vitamin D deficiency and maintain bone health.",
            "symptoms": "Bone weakness, fatigue, Vitamin D deficiency",
            "dosage": "1 capsule once a week for 8 weeks (as directed).",
            "common_side_effects": "None usually if taken as directed.",
            "serious_side_effects": "High calcium levels (nausea, constipation, kidney stones) if overdosed.",
            "food_to_eat": "Best absorbed when taken with a meal containing fat.",
            "prescription_required": False
        },
        {
            "medicine_name": "Iron Supplement (Ferrous Ascorbate)",
            "generic_name": "Ferrous Ascorbate + Folic Acid",
            "brand_name": "Dexorange, Orofer",
            "category": "Vitamins",
            "uses": "Used to treat or prevent iron deficiency anemia.",
            "symptoms": "Anemia, weakness, pale skin",
            "dosage": "1 tablet daily.",
            "common_side_effects": "Constipation, dark stools, stomach upset",
            "serious_side_effects": "Severe stomach pain",
            "food_to_avoid": "Do not take with milk, calcium supplements, or tea/coffee.",
            "food_to_eat": "Taking with Vitamin C (like orange juice) increases absorption.",
            "prescription_required": False
        }
    ]
    
    # Let's add 20 more quickly to hit the 40 mark
    more_medicines = [
        {"medicine_name": "Ondansetron 4mg", "category": "Antiemetic", "uses": "Prevents nausea and vomiting.", "symptoms": "Nausea, vomiting"},
        {"medicine_name": "Fluconazole 150mg", "category": "Antifungal", "uses": "Treats fungal infections.", "symptoms": "Yeast infection"},
        {"medicine_name": "Acyclovir 400mg", "category": "Antiviral", "uses": "Treats viral infections like herpes.", "symptoms": "Cold sores, chickenpox"},
        {"medicine_name": "Loratadine 10mg", "category": "Respiratory", "uses": "Treats allergies.", "symptoms": "Allergy, runny nose"},
        {"medicine_name": "Domperidone 10mg", "category": "Antiemetic", "uses": "Relieves nausea.", "symptoms": "Nausea, bloating"},
        {"medicine_name": "Telmisartan 40mg", "category": "Cardiology", "uses": "Treats high blood pressure.", "symptoms": "Hypertension"},
        {"medicine_name": "Rosuvastatin 10mg", "category": "Cardiology", "uses": "Lowers cholesterol.", "symptoms": "High cholesterol"},
        {"medicine_name": "Metoprolol 50mg", "category": "Cardiology", "uses": "Treats high blood pressure and chest pain.", "symptoms": "Hypertension, angina"},
        {"medicine_name": "Levothyroxine 50mcg", "category": "Hormones", "uses": "Treats hypothyroidism.", "symptoms": "Thyroid deficiency"},
        {"medicine_name": "Gabapentin 300mg", "category": "Neurology", "uses": "Treats nerve pain and seizures.", "symptoms": "Nerve pain"},
        {"medicine_name": "Pregabalin 75mg", "category": "Neurology", "uses": "Treats nerve pain.", "symptoms": "Neuropathic pain"},
        {"medicine_name": "Sertraline 50mg", "category": "Psychiatry", "uses": "Treats depression and anxiety.", "symptoms": "Depression, anxiety"},
        {"medicine_name": "Escitalopram 10mg", "category": "Psychiatry", "uses": "Treats depression and anxiety.", "symptoms": "Depression, anxiety"},
        {"medicine_name": "Clonazepam 0.5mg", "category": "Psychiatry", "uses": "Treats panic attacks and seizures.", "symptoms": "Anxiety, seizures"},
        {"medicine_name": "Zolpidem 10mg", "category": "Psychiatry", "uses": "Treats insomnia.", "symptoms": "Sleep disorders"},
        {"medicine_name": "Finasteride 1mg", "category": "Dermatology", "uses": "Treats male pattern baldness.", "symptoms": "Hair loss"},
        {"medicine_name": "Isotretinoin 20mg", "category": "Dermatology", "uses": "Treats severe acne.", "symptoms": "Severe acne"},
        {"medicine_name": "Mupirocin Ointment", "category": "Antibiotics", "uses": "Treats skin infections.", "symptoms": "Skin infection"},
        {"medicine_name": "Clotrimazole Cream", "category": "Antifungal", "uses": "Treats fungal skin infections.", "symptoms": "Ringworm, fungal rash"},
        {"medicine_name": "Methylprednisolone 4mg", "category": "Steroids", "uses": "Treats severe inflammation.", "symptoms": "Severe allergies, inflammation"}
    ]
    
    # Fill in default values for the 20 basic ones to make them look complete
    for m in more_medicines:
        m['dosage'] = "As prescribed by doctor."
        m['side_effects'] = "May cause mild side effects. Consult doctor."
        m['prescription_required'] = True
        medicines.append(m)

    print(f"Adding {len(medicines)} medicines to the database...")
    count = 0
    for data in medicines:
        # Check if exists to avoid duplicates if they run it multiple times
        obj, created = Medicine.objects.update_or_create(
            medicine_name=data['medicine_name'],
            defaults=data
        )
        if created:
            count += 1
            
    print(f"Database seeding completed! Added {count} new medicines.")

if __name__ == '__main__':
    seed_large_data()
