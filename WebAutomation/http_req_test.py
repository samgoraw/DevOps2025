import requests

#post
data = {"name":"Sam Gourav Nag","username":"sam123","email":"sam.gourav19@gmail.com"}
response = requests.post('https://jsonplaceholder.typicode.com/users',json =data)
print(response.json())

#get
response = requests.get('https://jsonplaceholder.typicode.com/users/1')
print("Status Code",response.status_code)
data = response.json()
print("street",data["address"]["street"])
print("Suite",data["address"]["suite"])
print("City",data["address"]["city"])