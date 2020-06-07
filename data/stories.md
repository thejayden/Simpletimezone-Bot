## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_sorry
  - utter_iamabot

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## timezone long
* greet
  - utter_greet
* find_timezone
  - utter_ask_continent
  - utter_show_zones
  - action_show_zones
* continent_info
  - utter_ask_location
* city_info
  - utter_finding_timezone
  - action_show_timezone
* thanks
  - utter_you_are_welcome
  - utter_goodbye

## timezone short
* greet
  - utter_greet
* find_timezone_with_location
  - utter_ask_continent_short
  - utter_show_zones
  - action_show_zones
* continent_info  
  - utter_finding_timezone
  - action_show_timezone
* thanks
  - utter_you_are_welcome
  - utter_goodbye

## queries
* find_cities
  - utter_list_cities
  - action_show_cities
* find_timezone_with_location
  - utter_ask_continent_short
  - utter_show_zones
  - action_show_zones
* continent_info  
  - utter_finding_timezone
  - action_show_timezone
* thanks
  - utter_you_are_welcome
  - utter_goodbye

## random_city_input
* city_info
  - utter_ask_continent_short
  - utter_show_zones
  - action_show_zones
* continent_info
  - utter_finding_timezone
  - action_show_timezone  

