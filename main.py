from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

app = FastAPI()

class Patient(BaseModel):
    id:Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name:Annotated[str, Field(..., description='Name of the Patient')]
    city:Annotated[str, Field(..., description='City where the Patient is living')]
    age:Annotated[int, Field(..., gt=0, lt=90, description='Age of the Patient')]
    gender:Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the Patient')]
    height:Annotated[float, Field(..., gt=0, description='Height of the Patient in meters')]
    weight:Annotated[float, Field(..., gt=0, description='Weight of the Patient in Kgs')]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi <25:
            return "Normal"
        elif self.bmi <30:
            return 'Overweight'
        else:return 'Obese'

def load_data():
    with open('Patients.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('Patients.json', 'w') as f:
        json.dump(data, f)


@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get("/about")
def about():
    return {'message':'A fully functional API to manage your patient records.'}

@app.get('/view')
def view():
    patients_data = load_data()

    return patients_data


@app.get('/patient/{patient_id}')
def view_patient(patient_id:str = Path(..., description='ID of the patient in the DB', example='P001')):
    #load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get('/sort')
def sort_patients(sort_by:str = Query(..., description= 'Sort on the basis of height, weight or BMI'), order:str = Query('asc', description='sort in ascending or descending order')):
    valied_fields = ['height', 'weight', 'bmi']
    if sort_by not in valied_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valied_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail = 'Invalid order select from asc or desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by,0), reverse=sort_order)

    return sorted_data

@app.post('/create')
def create_patient(patient:Patient):
    #load existing data for validation
    data = load_data()

    #check if the patient already exist in the database
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    
    #Add new patient to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    #Save into json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'Patient created succesfully'})