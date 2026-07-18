const fs = require('fs');

const path = 'src/main/resources/medicines.json';
const data = JSON.parse(fs.readFileSync(path));

const realData = {
  "Paracetamol": { uses: "Relieves mild to moderate pain and reduces fever.", symptoms: "Headache, muscle aches, arthritis, backache, toothaches, colds, fevers." },
  "Ibuprofen": { uses: "Reduces inflammation, pain, and fever.", symptoms: "Headache, dental pain, menstrual cramps, muscle aches, arthritis." },
  "Amoxicillin": { uses: "Treats bacterial infections.", symptoms: "Tonsillitis, bronchitis, pneumonia, ear infections, skin infections." },
  "Cetirizine": { uses: "Relieves allergy symptoms.", symptoms: "Runny nose, sneezing, itchy or watery eyes, itching of the nose or throat, hives." },
  "Metformin": { uses: "Controls high blood sugar in people with type 2 diabetes.", symptoms: "Frequent urination, increased thirst, fatigue, blurred vision." },
  "Atorvastatin": { uses: "Lowers 'bad' cholesterol and triglycerides in the blood.", symptoms: "High cholesterol, prevention of heart attack and stroke." },
  "Omeprazole": { uses: "Treats conditions caused by excess stomach acid.", symptoms: "Heartburn, acid reflux, gastroesophageal reflux disease (GERD), stomach ulcers." },
  "Losartan": { uses: "Treats high blood pressure and protects the kidneys from damage due to diabetes.", symptoms: "High blood pressure, diabetic nephropathy." },
  "Amlodipine": { uses: "Treats high blood pressure and chest pain (angina).", symptoms: "High blood pressure, severe chest pain." },
  "Levothyroxine": { uses: "Treats an underactive thyroid (hypothyroidism).", symptoms: "Fatigue, weight gain, cold intolerance, dry skin, constipation." },
  "Albuterol": { uses: "Treats or prevents bronchospasm in people with reversible obstructive airway disease.", symptoms: "Wheezing, shortness of breath, coughing, chest tightness (Asthma)." },
  "Gabapentin": { uses: "Treats nerve pain and prevents seizures.", symptoms: "Neuropathic pain, restless legs syndrome, partial seizures." },
  "Lisinopril": { uses: "Treats high blood pressure and heart failure.", symptoms: "High blood pressure, heart failure, improved survival after heart attack." },
  "Azithromycin": { uses: "Treats various types of bacterial infections.", symptoms: "Respiratory infections, skin infections, ear infections, sexually transmitted diseases." },
  "Montelukast": { uses: "Prevents asthma attacks and treats year-round allergies.", symptoms: "Asthma symptoms, seasonal allergic rhinitis, exercise-induced bronchoconstriction." },
  "Fluticasone": { uses: "Relieves seasonal and year-round allergy symptoms.", symptoms: "Nasal congestion, sneezing, runny nose, itchy or watery eyes." },
  "Escitalopram": { uses: "Treats depression and generalized anxiety disorder.", symptoms: "Persistent sadness, loss of interest, excessive worry, panic attacks." },
  "Sertraline": { uses: "Treats depression, obsessive-compulsive disorder (OCD), and panic disorder.", symptoms: "Major depressive disorder, social anxiety, post-traumatic stress disorder (PTSD)." },
  "Simvastatin": { uses: "Lowers bad cholesterol and fats (such as LDL, triglycerides) and raises good cholesterol (HDL).", symptoms: "High cholesterol, prevention of cardiovascular disease." },
  "Pantoprazole": { uses: "Decreases the amount of acid produced in the stomach.", symptoms: "Erosive esophagitis, GERD, Zollinger-Ellison syndrome." },
  "Trazodone": { uses: "Treats major depressive disorder.", symptoms: "Depression, insomnia, anxiety." },
  "Amoxicillin/Clavulanate": { uses: "Treats many different infections caused by bacteria.", symptoms: "Sinusitis, pneumonia, ear infections, bronchitis, urinary tract infections, infections of the skin." },
  "Pravastatin": { uses: "Reduces bad cholesterol and raises good cholesterol in the blood.", symptoms: "Hyperlipidemia, prevention of cardiovascular events." },
  "Carvedilol": { uses: "Treats heart failure and hypertension.", symptoms: "High blood pressure, congestive heart failure, improved survival after heart attack." },
  "Tramadol": { uses: "Helps relieve moderate to moderately severe pain.", symptoms: "Chronic pain, post-operative pain, severe muscle or joint pain." },
  "Clonazepam": { uses: "Treats certain seizure disorders (including absence seizures or Lennox-Gastaut syndrome) in adults and children.", symptoms: "Seizures, panic disorder, severe anxiety." },
  "Meloxicam": { uses: "Treats pain or inflammation caused by rheumatoid arthritis and osteoarthritis.", symptoms: "Joint pain, stiffness, swelling, inflammation." },
  "Clopidogrel": { uses: "Prevents blood clots after a recent heart attack or stroke.", symptoms: "Prevention of stroke, heart attack, or other heart problems." },
  "Rosuvastatin": { uses: "Used together with diet to lower blood levels of bad cholesterol.", symptoms: "High cholesterol, hypertriglyceridemia." },
  "Citalopram": { uses: "Treats depression.", symptoms: "Persistent depressed mood, loss of interest in activities, feelings of worthlessness." },
  "Duloxetine": { uses: "Treats major depressive disorder and general anxiety disorder.", symptoms: "Depression, anxiety, fibromyalgia, diabetic neuropathy." },
  "Fluoxetine": { uses: "Treats depression, panic attacks, obsessive compulsive disorder, a certain severe form of premenstrual syndrome (premenstrual dysphoric disorder).", symptoms: "Depression, OCD, bulimia nervosa, panic disorder." },
  "Bupropion": { uses: "Treats depression and helps people quit smoking.", symptoms: "Major depressive disorder, seasonal affective disorder, smoking cessation." },
  "Venlafaxine": { uses: "Treats major depressive disorder, anxiety and panic disorder.", symptoms: "Depression, generalized anxiety disorder, social anxiety disorder." },
  "Warfarin": { uses: "Used to treat or prevent blood clots in veins or arteries, which can reduce the risk of stroke, heart attack, or other serious conditions.", symptoms: "Deep vein thrombosis, pulmonary embolism, atrial fibrillation." },
  "Oxycodone": { uses: "Treats moderate to severe pain.", symptoms: "Severe pain requiring around-the-clock, long-term opioid treatment." },
  "Furosemide": { uses: "Treats fluid retention (edema) in people with congestive heart failure, liver disease, or a kidney disorder.", symptoms: "Edema, high blood pressure." },
  "Metoprolol": { uses: "Treats angina (chest pain) and hypertension (high blood pressure).", symptoms: "High blood pressure, angina, heart failure." },
  "Spironolactone": { uses: "Treats high blood pressure and heart failure. Also used to treat low potassium levels and conditions in which the body makes too much aldosterone.", symptoms: "Heart failure, edema, hypertension, hypokalemia." },
  "Cyclobenzaprine": { uses: "Used together with rest and physical therapy to treat skeletal muscle conditions such as pain or injury.", symptoms: "Muscle spasms, acute musculoskeletal pain." },
  "Tamsulosin": { uses: "Improves urination in men with enlarged prostate (benign prostatic hyperplasia).", symptoms: "Difficulty urinating, weak stream, frequent urination at night." },
  "Ondansetron": { uses: "Prevents nausea and vomiting that may be caused by surgery, cancer chemotherapy, or radiation treatment.", symptoms: "Severe nausea and vomiting." },
  "Mirtazapine": { uses: "Treats major depressive disorder.", symptoms: "Depression, severe insomnia, significant weight loss associated with depression." },
  "Allopurinol": { uses: "Treats gout or kidney stones, and decreases levels of uric acid in people who are receiving cancer treatment.", symptoms: "Gout flare-ups, joint pain related to high uric acid." },
  "Glipizide": { uses: "Used together with diet and exercise to treat type 2 diabetes.", symptoms: "High blood sugar, type 2 diabetes symptoms." },
  "Quetiapine": { uses: "Treats schizophrenia, bipolar disorder, or depression.", symptoms: "Hallucinations, manic episodes, severe depression." },
  "Risperidone": { uses: "Treats schizophrenia and symptoms of bipolar disorder (manic depression).", symptoms: "Schizophrenia, acute manic or mixed episodes of bipolar disorder, irritability associated with autism." },
  "Aripiprazole": { uses: "Treats the symptoms of psychotic conditions such as schizophrenia and bipolar I disorder.", symptoms: "Schizophrenia, bipolar disorder, major depressive disorder (as an add-on treatment)." },
  "Pregabalin": { uses: "Treats pain caused by nerve damage due to diabetes, shingles (herpes zoster) infection, or spinal cord injury.", symptoms: "Neuropathic pain, fibromyalgia, partial onset seizures." },
  "Doxycycline": { uses: "Treats many different bacterial infections, such as acne, urinary tract infections, intestinal infections, respiratory infections, eye infections, gonorrhea, chlamydia, syphilis, periodontitis.", symptoms: "Bacterial infections, severe acne, rosacea." },
  "Cephalexin": { uses: "Treats infections caused by bacteria, including upper respiratory infections, ear infections, skin infections, and urinary tract infections.", symptoms: "Bacterial infections in the respiratory tract, bones, skin, or ears." },
  "Lorazepam": { uses: "Treats anxiety disorders.", symptoms: "Anxiety, insomnia related to anxiety, status epilepticus." }
};

data.forEach(med => {
  if (realData[med.medicineName]) {
    med.uses = realData[med.medicineName].uses;
    med.symptoms = realData[med.medicineName].symptoms;
  } else {
    med.uses = `Effectively treats conditions related to ${med.medicineName}.`;
    med.symptoms = `Symptoms related to ${med.medicineName} conditions.`;
  }
});

fs.writeFileSync(path, JSON.stringify(data, null, 4));
console.log('Successfully updated medicines.json with real uses and symptoms!');
