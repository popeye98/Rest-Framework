import requests
import json
# url="http://127.0.0.1:8000/api/users_list/"

# response=requests.get(url)

# print(response.text)

# get auth token


def get_token():
     
    url="http://127.0.0.1:8000/api/auth/"

    response=requests.post(url ,data={'username':"admin","password":"admin"})
    return response.json()



def get_data():
    url="http://127.0.0.1:8000/api/users_list/"
    
    header={'Authorization':f'Token {get_token()}'}
    response=requests.get(url,headers=header)
    emp_data=response.json()
    for e in emp_data:
        print(e)
def create_new(count):
    url="http://127.0.0.1:8000/api/users_list/"
    header={'Authorization':f'Token {get_token()}'}
    data={
   
    "name": "def",
    "age": 20,
    "ranking": 2.5,
    "employee_id": f"HQ00{count}",

}
    response=requests.post(url ,data=data,headers=header)
    print(response.text)
def edit_data(employee_id):
    url=f"http://127.0.0.1:8000/api/users_list/{employee_id}/"
    header={'Authorization':f'Token {get_token()}'}
    data={
   
    "name": "mnp",
    "age": 25,
    "ranking": 5.5,
    

}
    response=requests.put(url ,data=data,headers=header)
    print(response.text)

def delete_data(employee_id):
    url=f"http://127.0.0.1:8000/api/users_list/{employee_id}/"
    header={'Authorization':f'Token {get_token()}'}
    response=requests.delete(url ,headers=header)
    print(response.status_code)
    
delete_data(5)