from random import randint

drug_list = []
drug_list.append({
    'name': 'Loxapine',
    'relieves' : ['adhd', 'anxiety'],
    'side_effects': 'Swelling of the tongue, involuntary tongue thursting, mask-like expression of the face, constant need to move'
})
drug_list.append({
    'name': 'Diazepam',
    'relieves' : ['anxiety'],
    'side_effects': 'Hallucinations, yellowing eyes, trouble speaking, blurred vision'
})
drug_list.append({
    'name': 'Lisinopril',
    'relieves' : ['hypertension'],
    'side_effects' : 'tongue swelling, high potassium blood, severe dizziness'
})
drug_list.append({
    'name': 'Enalapril',
    'relieves' : ['hypertension'],
    'side_effects': 'decrease in vision, vp,otomg. easy bruising/bleeding, extreme dry throat/mouth'
})
drug_list.append({
    'name': 'Captopril',
    'relieves' : ['hypertension'],
    'side_effects': 'High potassium levels, signs of infection, cloudy urine, persistant vomiting'
})
drug_list.append({
    'name': 'Nadolol',
    'relieves' : ['chest pain', 'hypertension'],
    'side_effects': 'Blue nails, hair loss, numbness, swelling of extremities'
})
drug_list.append({
    'name': 'Bisoprolol',
    'relieves' : ['hypertension'],
    'side_effects': 'Eye pain, hair loss, loss of feeling/tingling, extreme throat, trouble breathing'
})
drug_list.append({
    'name': 'Timolol',
    'relieves' : ['eye pressure'],
    'side_effects': 'Blurred vision, burning sensation, watery eye, dry eyes'
})
drug_list.append({
    'name': 'Pindolol',
    'relieves' : ['hypertension'],
    'side_effects': 'Blue nails, cold hands/feet, pain/cramps, hair loss'
})
drug_list.append({
    'name': 'Glutathione',
    'relieves' : ['nausea', 'fever', 'rheumatic fever', 'vomiting', 'cough', 'hoarseness'],
    'side_effects': 'You can stop breathing, cough, shortness of breath, chest pain'
})
drug_list.append({
    'name': 'Hydrocortisone',
    'relieves' : ['itching', 'bites', 'stings', 'rash', 'allergies'],
    'side_effects': 'Your skin may start burning'
})
drug_list.append({
    'name': 'Dexamethasone',
    'relieves' : ['itching', 'bites', 'stings', 'rash', 'allergies'],
    'side_effects': "Irregular heartbeat, vomit that looks like coffee grounds, seizures"
})
drug_list.append({
    'name': 'Prednisolone',
    'relieves' : ['rash', 'cough', 'hoarseness', 'pain', 'itching'],
    'side_effects': 'Bleeding from the stomach or intestines, chest pain, seizures'
})
drug_list.append({
    'name': 'Methylprednisolone',
    'relieves' : ['fever', 'rheumatic fever' , 'itching', 'rash', 'cough', 'hoarseness'],
    'side_effects': 'Trouble breathing, vision problems, abdominal bleeding'
})
drug_list.append({
    'name': 'Prazosin',
    'relieves' : ['hypertension'],
    'side_effects': 'Fainting, blurred vision, nausea, vomiting'
})
drug_list.append({
    'name': 'Doxazosin',
    'relieves' : ['hypertension'],
    'side_effects': 'Yellowing eyes and skin, swelling of the face, tongue, and throat, fainting'
})
drug_list.append({
    'name' : 'Alfuzosin' ,
    'relieves' : ['hypertension'],
    'side_effects': 'Chest pain, fainting, yellowing eyes and skin'
})
drug_list.append({
    'name': 'Propanolol',
    'relieves' : ['headache', 'pain', 'muscle cramps', 'hypertension'],
    'side_effects': 'Fainting, trouble breathing, swollen joints, blue fingers and toes'
})
drug_list.append({
    'name': 'Metoprolol',
    'relieves' : ['pain', 'hypertension'], 
    'side_effects': 'slow heart, severe dizziness, pain in hands and feet'
})


def get_drug(symptom):
    symptom = symptom.lower()
    possible_drugs = []
    for i in range(len(drug_list)):
        for j in range(len(drug_list[i]['relieves'])):
            if symptom in drug_list[i]['relieves'][j]:
                possible_drugs.append(i)
    if (len(possible_drugs) == 0):
        return False
    x = possible_drugs[randint(0, (len(possible_drugs)-1))]
    return drug_list[x]['name'], drug_list[x]['relieves'],drug_list[x]['side_effects']

