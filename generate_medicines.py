import json
import random

medicine_names = [
    "Paracetamol", "Ibuprofen", "Amoxicillin", "Cetirizine", "Metformin", "Atorvastatin", "Omeprazole",
    "Losartan", "Amlodipine", "Levothyroxine", "Albuterol", "Gabapentin", "Lisinopril", "Azithromycin",
    "Montelukast", "Fluticasone", "Escitalopram", "Sertraline", "Simvastatin", "Pantoprazole",
    "Trazodone", "Amoxicillin/Clavulanate", "Pravastatin", "Carvedilol", "Tramadol", "Clonazepam",
    "Meloxicam", "Clopidogrel", "Rosuvastatin", "Citalopram", "Duloxetine", "Fluoxetine", "Bupropion",
    "Venlafaxine", "Warfarin", "Oxycodone", "Furosemide", "Metoprolol", "Spironolactone", "Cyclobenzaprine",
    "Tamsulosin", "Ondansetron", "Mirtazapine", "Allopurinol", "Glipizide", "Quetiapine", "Risperidone",
    "Aripiprazole", "Pregabalin", "Doxycycline", "Cephalexin", "Lorazepam"
]

categories = [
    "Pain Relievers", "Antibiotics", "Cardiology", "Respiratory", "Antihistamines", "Gastrointestinal",
    "Endocrinology", "Neurology", "Psychiatry", "Dermatology"
]

medicines = []
for i, name in enumerate(medicine_names):
    med = {
        "medicineName": name,
        "genericName": name + " Generic",
        "brandName": name + " Brand",
        "category": random.choice(categories),
        "uses": f"Used to treat conditions related to {name}.",
        "dosage": "Adults: 1 tablet daily. Do not exceed recommended dose.",
        "sideEffects": "Dizziness, nausea, headache.",
        "commonSideEffects": "Nausea, mild headache.",
        "seriousSideEffects": "Severe allergic reactions, shortness of breath.",
        "foodToEat": "Take with water. Can be taken with food to avoid stomach upset.",
        "foodToAvoid": "Avoid alcohol and grapefruit juice.",
        "alcoholWarning": "WARNING: Consuming alcohol with this medication may increase side effects.",
        "pregnancySafety": "Consult your doctor before taking if pregnant or breastfeeding.",
        "breastfeedingSafety": "Consult a doctor before use while breastfeeding.",
        "kidneyWarning": "Dose adjustment may be necessary for patients with kidney disease.",
        "liverWarning": "Use with caution if you have liver impairment.",
        "childrenSafety": "Not recommended for children under 12 unless prescribed.",
        "elderlySafety": "Safe for the elderly at recommended doses.",
        "drivingWarning": "May cause dizziness. Do not drive until you know how this medication affects you.",
        "drugInteractions": "May interact with blood thinners, certain antibiotics, and antifungals.",
        "diseaseInteractions": "Use with caution in patients with heart, liver, or kidney disease.",
        "prescriptionRequired": random.choice([True, False]),
        "manufacturer": "PharmaCorp Generic",
        "description": f"{name} is a reliable medication for its specified use cases, offering relief with standard dosages."
    }
    medicines.append(med)

with open(r"c:\Users\sakthi paramesh\OneDrive\Documents\medsafety\src\main\resources\medicines.json", "w") as f:
    json.dump(medicines, f, indent=4)

print("Generated 50+ medicines successfully.")
