# OIBSIP_domain_taskno.3
Objectives 
    1.Responding to greeting like hello 
    2.Telling current time and date 
    3.Searching for webs asked by user
    4.Providing default replies when not audible or don't understand commands

Tools used
    1.speech_recognition library
    2.pyttsx3 library
    3.pywhatkit library
    4.datetime library

Steps performed
    1.setup of microphone listening using speech_recognition
    2.voice settings using pyttxs3
    3.used microphone for capturing user speech
    4.this speech is converted to text using goggle's API
    5. checks user command and if command contains following keyword 
       hello= response with greeting 
       time= tells current time 
       date=tells current date
       " search <query> " = searches web
    6.uses pyttsx3 to speak the assistant response
    7.prints user voice input and asssistant reply
    8.stops the exection when user say exit 

Outcome

   1.understands natural voice commands and interact with it
   2.performs basic task like giving greetings and opening websites
