#this file contains all the functions required for the actions file to call

import requests

addr="http://api.timezonedb.com/v2.1/get-time-zone?key=2IR59YRTL3BM&format=json&by=zone&zone={}/{}"
addr2="http://api.timezonedb.com/v2.1/list-time-zone?key=2IR59YRTL3BM&format=json"
zones = ['Asia','America', 'Africa', 'Europe', 'Antarctica','Pacific','Indian','Atlantic', 'Australia']

#function to get the time of a city with the zone and city name as parameters
def getTime(continent, city):
    
    api_addr = addr.format(continent,city)
    api_json = requests.get(api_addr).json()
    cmbndString = api_json['formatted']
    return cmbndString.split()[1]

#get the date from API
def getDate(continent, city):
    
    api_addr = addr.format(continent,city)
    api_json = requests.get(api_addr).json()
    cmbndString = api_json['formatted']
    return cmbndString.split()[0]

#returns the status of request from API to check if zone and city is valid 
def checkError(continent, city):
    
    api_addr = addr.format(continent,city)
    api_json = requests.get(api_addr).json()
    return api_json['status']

#function to get GMT (unused)
def getGMT(continent, city):
   
    api_addr = addr.format(continent,city)
    api_json = requests.get(api_addr).json()
    seconds = api_json['gmtOffset']
    hours = seconds/3600
    
    #return print(f"GMT +{hours:.2f}")
    return print("GMT +{}hrs".format(round(hours)))

#get the zones listed in API. "zones" is a predefined list created for convenience sake 
def getZones():
   
    zones.sort()
    return zones

#returns a list of available cities in the API
def getCities():
    
    #parse API as json
    api_json = requests.get(addr2).json()
    listCities = []

    #use for loop to extract all "zoneName" which contains the data of the zone and city in this manner "{zone}/{city}" e.g. "asia/singapore"
    for each in api_json['zones']:
        zoneNameStr = each['zoneName']
        #split method to get city name
        cityName = zoneNameStr.split('/')[1]
        #some "zoneName" contains an extra region field e.g. "{zone}/{region}/{city}". Check for extra region field and proceed to extract real city name if field exists.
        if cityName == 'Argentina' or cityName == 'Indiana' or cityName == 'Kentucky' or cityName == 'North_Dakota':
            cityRealName = zoneNameStr.split('/')[2]
            listCities.append(cityRealName)
        else:
            listCities.append(cityName)
    #sort and return list that contains all city names
    listCities.sort()
    return listCities 

#function to get all the "zoneName" and print the list (unused)
def getAll():
    
    api_json = requests.get(addr2).json()
    listZones = []

    for each in api_json['zones']:
        zoneNameStr = each['zoneName']
        listZones.append(zoneNameStr)
    
    listZones.sort()
    print(*listZones, sep = "\n")
