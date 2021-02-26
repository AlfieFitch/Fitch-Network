import requests
import json

users = []


def embgetuserid(name):
    final = []
    found=[]
    counter = 0
    response = requests.get('http://192.168.1.218:8069/jellyfin/Users?api_key=5e851c55a6734f0683f10ab099cd39ee')
    response = response.text
    response = response.split('}},')
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
        if '"Id' not in final[counter]:
            counter = counter + 1
        else:
            foundid = final[counter]
            break
    finalid = foundid.replace('"','')
    finalid = finalid.replace("Id",'')
    finalid = finalid.replace(":",'')
    return("Emby id for " +  name + " = " + finalid)




def embnewuser(name, password):
    response = requests.post('http://192.168.1.218:8069/jellyfin/Users/New?api_key=5e851c55a6734f0683f10ab099cd39ee', data={'Name': name ,'Password': password})
    embgetuserid(name)


def embdeleteuser():
    id = getuserid()
    print(id)
    response = requests.delete('http://192.168.1.218:8069/jellyfin/Users/' + id + '?api_key=5e851c55a6734f0683f10ab099cd39ee')
    print(response)
