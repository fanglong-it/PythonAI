import speech_recognition
import pyttsx3
import os 
from datetime import date
from datetime import datetime


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
cont = True

#Listen
while True:
        
        with speech_recognition.Microphone() as mic:
            robot_ear.adjust_for_ambient_noise(mic,duration=4)
            #robot_ear.energy_threshold()
            print("I'm Listening : ")
            audio= robot_ear.listen(mic)
            print("Robot:...")
          
        try:
                you = robot_ear.recognize_google(audio)
                print("You: " + you)
        except:
                you = ""
#AI understand
        if you == "":
                robot_brain = "I can't hear you, what i can help you?"
        elif you == "hello":
                robot_brain = "Hello Fanglong, what i can help you?"
                
        elif you == "hey bro":
                robot_brain = "Hey what's up bro, what can i help u?"
                
        elif you == "what is today":
                today = date.today()
                stringDate = today.strftime("%A, %d %b %Y")
                robot_brain = "Its " + stringDate
        elif you == "what's today":
                today = date.today()
                stringDate = today.strftime("%A, %d %b %Y")
                robot_brain = "Its " + stringDate
        elif you == "what's the date":
                today = date.today()
                stringDate = today.strftime("%A, %d %b %Y")
                robot_brain = "Its " + stringDate
        elif you == "what is the time":
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                robot_brain = "It's "+current_time + " O'clock"
        elif you == "what's the time":
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                robot_brain = "It's "+current_time + " O'clock"

        elif you == "president of America":
                robot_brain = "Donald Trump"
                
        elif you == "exit":
                robot_brain = "Goodbye Fanglong"
                print(robot_brain)
                voices = robot_mouth.getProperty('voices')
                robot_mouth.setProperty('voice',voices[1].id)
                robot_mouth.say(robot_brain)
                robot_mouth.runAndWait()
                break
        elif you == "bye":
                robot_brain = "Goodbye Fanglong"
                print(robot_brain)
                voices = robot_mouth.getProperty('voices')
                robot_mouth.setProperty('voice',voices[1].id)
                robot_mouth.say(robot_brain)
                robot_mouth.runAndWait()
                break
                
        else :
                robot_brain = "I can't understand, what i can help you?"
#Speech           
        print(robot_brain)
        voices = robot_mouth.getProperty('voices')
        robot_mouth.setProperty('voice', voices[1].id)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()

        
