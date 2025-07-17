from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name:Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish','Krish'])]
    email:EmailStr
    linkedIn_Url: AnyUrl
    age:int=Field(description="Age", gt=0, lt=89)
    weight:Annotated[float, Field(gt=0, strict=True)]
    married:Annotated[bool, Field(default=None, description="Is the patient married or not")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details:Dict[str, str]

    print('inserted')

patient_info = {'name':'nitish', 'age':30, 'weight':75.2, 'married':True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com','phone':'12332223'}}


patient1 = Patient(**patient_info)

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.weight)
    print(patient.contact_details)
    print('inserted')

insert_patient_data(patient1)