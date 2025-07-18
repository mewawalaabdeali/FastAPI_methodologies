from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model
    

def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')


patient_info = {
    'name':'nitish',
    'email':'abc@icici.com',
    'age':'65',
    'weight':75.8,
    'married':True,
    'allergies':['pollen', 'dust'],
    'contact_details':{
        'phone':'9827654321',
        'emergency':'775556233'
    }
}

patient1 = Patient(**patient_info)

update_patient(patient1)
    

