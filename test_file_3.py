import requests

addr="http://api.timezonedb.com/v2.1/list-time-zone?key=2IR59YRTL3BM&format=json"

api_json = requests.get(addr).json()
zones = api_json['zones'][1]['zoneName']
print(zones +'\n')
listCities = []

for each in api_json['zones']:
    zoneNameStr = each['zoneName']#.split('/')[1]
    cityName = zoneNameStr.split('/')[1]
    if cityName == 'Argentina' or cityName == 'Indiana' or cityName == 'Kentucky' or cityName == 'North_Dakota':
        cityRealName = zoneNameStr.split('/')[2]
        listCities.append(cityRealName)
    else:
        listCities.append(cityName)
listCities.sort()
print(*listCities, sep = "\n")
print(len(listCities))