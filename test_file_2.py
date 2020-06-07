from newtimeAPI import getGMT, getDate, getTime, checkError, getZones

continent = "asia"
city ="singapore"

getZones()
getGMT(continent,city)
print(getTime(continent,city))
#print(getDate(continent,city))

'''out = checkError(continent,city)

print(out)

if out == 'OK' :
    print("Great")
else:
    print("Shit")'''


