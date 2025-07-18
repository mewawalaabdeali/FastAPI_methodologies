from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact:Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    

def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI',patient.bmi)
    print('updated')

patient_info = {
    'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'height': 1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact':{'phone':'2353462', 'emergency':'235236'}
}

patient1 = Patient(**patient_info)

update_patient(patient1)