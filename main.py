#task1 process voice to text
#Task2 Process the input and search for answer
#Please check readme file to see how to install required libraries first

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from datetime import datetime

def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(answer)
    engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    answer = 'You are speaking to AI voice assistant, How can I help!'
    print('Voice Assistant:', answer)
    talk(answer)
    print("listening....")
    audio = r.listen(source)

try:
    #print(r.recognize_google(audio))
    question = r.recognize_google(audio)
    if 'Alexa' in question:
        question = question.replace('Alexa','')
        #print(question)


    if 'what are you doing' in question:
        print("Human:", question)
        answer = ('I am waiting for your question')
        print('Voice Assistant:', answer)
        talk(answer)


    elif 'how are you' in question:
        print("Human:", question)
        answer = ('I am doing good, how are you dear')
        talk(answer)
        print('Voice Assistant:', answer)


    elif 'play' in question:
        print("Human:", question)
        question = question.replace('play', '')
        pywhatkit.playonyt(question)


    elif 'tell me about' in question:
        print("Human:", question)
        question = question.replace('tell me about', '')
        wiki = wikipedia.summary(question, 1)
        print(wiki)
        talk(wiki)


    elif 'time' in question:
        print("Human:", question)
        time = datetime.today().time().strftime('%I:%M %p')
        print(time)
        talk(time)


    elif 'joke' in question:
        print("Human:", question)
        joke = pyjokes.get_joke()
        print(pyjokes.get_joke())


    elif 'age' in question:
        print("Human:", question)
        question = question.replace('age', '')
        answer = ('Why do you want my age fuckig bitch')
        talk(answer)


    elif 'what does' in question:
        print("Human:", question)
        question = question.replace('what does', '')
        answer = ('nani')
        talk(answer)

    elif 'weather' in question:
        print("Human:", question)
        question = question.replace('weather', '')
        answer = get_weather('london')
        talk(answer)


    else:
        question = r.recognize_google(audio)
        print("Voice Assistant: sorry,I can't find answer to", question)
        answer = ("sorry,I can't find answer to", question, "Good Bye")
        print("Good Bye")
        talk(answer)


except sr.UnknownValueError:
    answer = "Since No response from you, Good bye for now"
    print("Since No Response from you, Good bye for now")
    talk(answer)
