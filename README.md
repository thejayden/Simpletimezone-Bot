![Alt Text](https://github.com/thejayden/Simpletimezone-Bot/blob/master/demo_gif.gif)
<br><sub> *View a smoother video version in ["demo_full.mp4"](https://github.com/thejayden/Simpletimezone-Bot/raw/master/demo_full.mp4) (download vid)* </sub>

## Simpletimezone-Bot
A chatbot made with rasa which tells the user the time in different cities. It retrieves information through API and returns the required information.
<br>
### File Breakdown
***
#### Intents & stories
The data folder contains *"nlu.md"* and *"stories.md"* files. <br>
*"nlu.md"* contains the intents while *"stories.md"* contains the story flows.

#### Domain
*"domain.yml"* defines the universe in which the assistant operates. Contains and specifies all the intents, entities, slots, actions and responses for the chatbot.

#### Main Action Template
*"actions.py"* contains the modified python template which allows the bot to perform tasks. 

#### Functions
*"newtimeAPI.py"* contains all the predefined functions for the action file to call to. (e.g. functions like getting the list of cities from API)

#### Other Python Files
The rest of the python files are for testing and debugging purposes.
