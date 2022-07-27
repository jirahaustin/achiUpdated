from backend.symptoms import *
from database.database import *
from backend.diagnosis import *

# NOTE: PATIENT RECORD IMPLEMENTATION (DATABASE)
# NOTE: NOT YET CONNECTED TO THE GRAPHICAL USER INTERFACE
Juan = {
    "date": "2022-07-23",
    "fname": "Juan",
    "lname": "Dela Cruz",
    "mname": "Sebastian",
    "bday": "2000-01-02",
    "age": 22,
    "sex": "male",
    "civil_status": "single",
    "tel_num": "09123456789",
    "address": "Brgy. Junel",
    "emergency_contact": {
        "full_name": "Juana Dela Cruz",
        "relationship": "Mother",
        "emergency_tel_num": "09876543219"
    },
    "symptoms": ["Headache", "Nausea", "Vertigo"],
    "results": {
        "prediction": "Malaria",
        "confidence_rating": "Very Likely",
        "causes": ["Cause 1", "Cause 2", "Cause 3"],
        "recommendations": [
            "Recommendation 1",
            "Recommendation 2",
            "Recommendation 3"
        ]
    }
}

Maria = {
    "date": "2022-07-23",
    "fname": "Maria",
    "lname": "Clara",
    "mname": "Juana",
    "bday": "2000-01-02",
    "age": 22,
    "sex": "male",
    "civil_status": "single",
    "tel_num": "09123456789",
    "address": "Brgy. Junel",
    "emergency_contact": {
        "full_name": "Juana Dela Cruz",
        "relationship": "Mother",
        "emergency_tel_num": "09876543219"
    },
    "symptoms": ["Headache", "Nausea", "Vertigo"],
    "results": {
        "prediction": "Malaria",
        "confidence_rating": "Very Likely",
        "causes": ["Cause 1", "Cause 2", "Cause 3"],
        "recommendations": [
            "Recommendation 1",
            "Recommendation 2",
            "Recommendation 3"
        ]
    }
}

# DATABASE / PATIENT RECORD
create_tables()
# ADD PATIENT RECORD (THIS INCLUDES THE RESULTS OF HIS DIAGNOSIS)
# add_record(Juan)
# ADD PATIENT RECORD (THIS INCLUDES THE RESULTS OF HER DIAGNOSIS)
add_record(Maria)
print(get_unique_patients())  # RETRIEVE THE LIST OF UNIQUE PATIENTS
# print(get_record(Juan))  # RETRIEVE A SPECIFIC PATIENT RECORD
# print(get_all_records())  # RETRIEVE ALL RECORDS
# print(get_summary())


# BACKEND
selected_symptoms = ['chills', 'constipation',
                     'abdominal_pain', 'belly_pain', 'diarrhoea']
# print(diagnosis(selected_symptoms))
# print(get_interview_symptoms(selected_symptoms))

# symptoms
symptom_category = "back"
# print(get_all_symptoms())
# print(get_symptoms(symptom_category))
