import requests
import json

URL = "http://127.0.0.1:8000/stu/"

#to fetch the data from database
def get_data(id=None):
    data={}

    if id is not None:
        data={'id':id}

    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)


#enter the new data in database
def post_data():
    data={
'name':'artharv',
'roll':190,
'city':'shimla'
        }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)


#for updating the data in database
def update_data():
    data={
'id':2,
'name':'rahul',
'roll':139,
'city':'shillong'
        }
    json_data=json.dumps(data)

    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

#delete the data provided in the id"
def delete_data():
    data={'id':1}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

#driver program
print('what do you want to do: ')
option={1:'GET',2:'POST',3:'UPDATE',4:'DELETE'}
print(option)
x=input('enter the key from above in capitals: ')
if x=='GET':
    get_data()
elif x=='POST':
    post_data()
elif  x=='UPDATE':
    update_data()
elif x=='DELETE':
    delete_data()
