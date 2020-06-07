#Unused file. Tried to use this API initially but it was restricted. 
import requests

def getTime(city):
    addr="https://www.amdoren.com/api/timezone.php?api_key=jbxcgDx32Kq2kLzStmPpu9YfAj9Pjd&loc={}"
    api_addr = addr.format(city)
    api_json = requests.get(api_addr).json()
#    print("The time is {}".format(api_json['time']))
    return api_json['time']

def checkError(city):
    addr="https://www.amdoren.com/api/timezone.php?api_key=jbxcgDx32Kq2kLzStmPpu9YfAj9Pjd&loc={}"
    api_addr = addr.format(city)
    api_json = requests.get(api_addr).json()
    return api_json['error']
