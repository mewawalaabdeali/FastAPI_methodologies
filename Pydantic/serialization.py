from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dic = {'city':'jersey', 'state':'new jersey', 'pin':'07306'}
address1 = Address(**address_dic)

patient_dic = {'name':'ali','gender':'male','age':31, 'address':address1}

patient1 = Patient(**patient_dic)

temp = patient1.model_dump(include=['name'])
temp1 = patient1.model_dump(exclude={'address':['state']})
temp_json = patient1.model_dump_json()
print(temp)

print(type(temp))