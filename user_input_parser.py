drug_list = {}
drug_list['drugs'] = []
drug_list['drugs'].append({
    'name': 'Loxapine',
    'relieves' : 'anxiety', #'adhd',
    'side_effects': 'Swelling of the tongue, involuntary tongue thursting, mask-like expression of the face, constant need to move'
})
drug_list['drugs'].append({
    'name': 'Diazepam',
    'relieves' : 'anxiety',
    'side_effects': 'Hallucinations, yellowing eyes, trouble speaking, blurred vision'
})
drug_list['drugs'].append({
    'name': 'Lisinopril',
    'relieves' : 'hypertension',
    'side_effects' : 'tongue swelling, high potassium blood, severe dizziness'
})
drug_list['drugs'].append({
    'name': 'Enalapril',
    'relieves' : 'hypertension',
    'side_effects': 'decrease in vision, vp,otomg. easy bruising/bleeding, extreme dry throat/mouth'
})
drug_list['drugs'].append({
    'name': 'Captopril',
    'relieves' : 'hypertension',
    'side_effects': 'High potassium levels, signs of infection, cloudy urine, persistant vomiting'
})
drug_list['drugs'].append({
    'name': 'Nadolol',
    'relieves' : 'hypertension', #'pain',
    'side_effects': 'Blue nails, hair loss, numbness, swelling of extremities'
})
drug_list['drugs'].append({
    'name': 'Bisoprolol',
    'relieves' : 'hypertension',
    'side_effects': 'Eye pain, hair loss, loss of feeling/tingling, extreme throat, trouble breathing'
})
drug_list['drugs'].append({
    'name': 'Timolol',
    'relieves' : 'eye pressure',
    'side_effects': 'Blurred vision, burning sensation, watery eye, dry eyes'
})
drug_list['drugs'].append({
    'name': 'Pindolol',
    'relieves' : 'hypertension',
    'side_effects': 'Blue nails, cold hands/feet, pain/cramps, hair loss'
})
drug_list['drugs'].append({
    'name': 'Glutathione',
    'relieves' : 'nausea', #'fever/rheumatic fever', 'vomiting', 'cough/hoarseness',
    'side_effects': 'You can stop breathing, cough, shortness of breath, chest pain'
})
drug_list['drugs'].append({
    'name': 'Hydrocortisone',
    'relieves' : 'itching', #'bites and stings', 'rash', 'allergies',
    'side_effects': 'Your skin may start burning'
})
drug_list['drugs'].append({
    'name': 'Dexamethasone'
    'relieves' : 'itching', #'bites and stings', 'rash, 'allergies',
    'side_effects': "Irregular heartbeat, vomit that looks like coffee grounds, seizures"
})
drug_list['drugs'].append({
    'name': 'Prednisolone',
    'relieves' : 'rash', #'cough/hoarseness', 'pain', 'itching',
    'side_effects': 'Bleeding from the stomach or intestines, chest pain, seizures'
})
drug_list['drugs'].append({
    'name': 'Methylprednisolone',
    'relieves' : 'fever/rheumatic fever', #'itching', 'rash', 'cough/hoarseness'
    'side_effects': 'Trouble breathing, vision problems, abdominal bleeding'
})
drug_list['drugs'].append({
    'name': 'Prazosin',
    'relieves' : 'hypertension',
    'side_effects': 'Fainting, blurred vision, nausea, vomiting'
})
drug_list['drugs'].append({
    'name': 'Doxazosin',
    'relieves' : 'hypertension',
    'side_effects': 'Yellowing eyes and skin, swelling of the face, tongue, and throat, fainting'
})
drug_list['drugs'].append({
    'name' : 'Alfuzosin' ,
    'relieves' : 'hypertension',
    'side_effects': 'Chest pain, fainting, yellowing eyes and skin'
})
drug_list['drugs'].append({
    'name': 'Propanolol',
    'relieves' : 'headache', #'pain', 'muscle cramp'. 'hypertension'
    'side_effects': 'Fainting, trouble breathing, swollen joints, blue fingers and toes'
})
drug_list['drugs'].append({
    'name': 'Metoprolol',
    'relieves' : 'hypertension', #'pain'
    'side_effects': 'slow heart, severe dizziness, pain in hands and feet'
})


def get_drug(symptom):
    for i in drug_list:
        for j in range(0,len(drug_list[i])):
            if(symptom == drug_list[i][j]['relieves']):
                return drug_list[i][j]['name'], drug_list[i][j]['relieves'], drug_list[i][j]['side_effects']

print(get_drug('x'))
