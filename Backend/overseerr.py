import requests
import json

setheaders={'X-Api-Key': 'MTYxMzc1MzE4MjE5OWMwZmUwYWIzLTFkYzktNDIwZi1iZjIwLWUwZjRiNjAwZTZiNSk='}


def overnewuser(name, email, password):
    response = requests.post('http://192.168.1.218:5055/api/v1/user', json= {'email': email , 'password' : password , 'username': name} , headers=setheaders)
    overfindid(name)

def overfindid(name):
    users = []
    final = []
    found = []
    counter = 0
    response = requests.get('http://192.168.1.218:5055/api/v1/user', headers=setheaders)
    response = response.text
    response = response.split('},{')
    for i in response:
        users.append(i)
    tofind = name
    while counter <= len(users):
        if tofind not in users[counter]:
            counter = counter + 1
        else:
            found.append(users[counter])
            break
    new = users[counter].split(',')
    for i in new:
        final.append(i)
    counter = 0
    while counter <= len(final):
        if 'id' not in final[counter]:
            counter = counter + 1
        else:
            foundid = final[counter]
            break
    finalid = foundid.replace('"','')
    finalid = finalid.replace("id",'')
    finalid = finalid.replace(":",'')
    return("Overseer Id for " + name + " = " + finalid)
