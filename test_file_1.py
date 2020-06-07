import requests
import re

addr="http://api.timezonedb.com/v2.1/get-time-zone?key=2IR59YRTL3BM&format=json&by=zone&zone={}/{}"
city = input("Enter City Name: ")
city = city.replace(" ", "_")
print(city)
continent=input("Enter Continent Name:")    
api_addr = addr.format(continent,city)
api_json = requests.get(api_addr).json()
print("The time is {}".format(api_json['formatted']))
print(api_json['status'])
print(type(api_json['status']))



