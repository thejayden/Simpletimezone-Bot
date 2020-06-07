# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from newtimeAPI import checkError, getTime, getDate, getZones, getCities, getAll
import re

class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_timezone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #get entity "city" from user input
        cityEnt = tracker.get_slot("city")
        #replace white space with underscore for correct API link
        cityConvert = cityEnt.replace(" ", "_")
        #get entity "continent" from user input
        continent = tracker.get_slot("continent")
        #check for correct inputs
        checkStr = checkError(continent,cityConvert)
        
        if checkStr == 'OK' :
            time = getTime(continent, cityConvert)
            output = "Time zone of {} is {}".format(cityEnt,time)
        else : 
            output = "Could not find time zone of {}. You might have entered the wrong zone. Please try again.".format(cityEnt)
        
        dispatcher.utter_message(text=output)

        return []

#to list all the available zones in the API (I predefined the list as there are only a few zones)
class ActionShowContinents(Action):

    def name(self) -> Text:
        return "action_show_zones"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        zones = getZones()
        output=''
        for x in range(len(zones)-1):
            output += "{}, ".format(zones[x])
        
        #format the last element without ","
        output += "{}".format(zones[-1])
        dispatcher.utter_message(text = output)        

        return []

#to list all the available cities in the API
class ActionShowCities(Action):

    def name(self) -> Text:
        return "action_show_cities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        listCities = getCities()
        output = ["","","","","","","","",""]

        #output messages in shorter lengths as messenger is unable to support too much text
        for x in range(len(listCities)):
            if x <= 50:
                output[0] += "{}, ".format(listCities[x])
                
            if 50 < x <=100:
                output[1] += "{}, ".format(listCities[x])
                
            if 100 < x <=150:
                output[2] += "{}, ".format(listCities[x])
                
            if 150 < x <=200:
                output[3] += "{}, ".format(listCities[x])
                
            if 200 < x <=250:
                output[4] += "{}, ".format(listCities[x])
            
            if 250 < x <=300:
                output[5] += "{}, ".format(listCities[x])
            
            if 300 < x <=350:
                output[6] += "{}, ".format(listCities[x])
            
            if 350 < x <=400:
                output[7] += "{}, ".format(listCities[x])

            if 400 < x < 424:
                output[8] += "{}, ".format(listCities[x])
        
        #format the last element without ","
        output[8] += "{}".format(listCities[-1])

        for i in range(len(output)):
            dispatcher.utter_message(text = output[i])

        return []