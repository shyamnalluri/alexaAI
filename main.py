#task1 process voice to text
#Task2 Process the input and search for answer

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from datetime import datetime
import pyjokes
from Py_Weather import get_weather


def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(answer)
    engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Hello, How can I help!')
    audio = r.listen(source)

try:
    #print(r.recognize_google(audio))
    question = r.recognize_google(audio)
    if 'Alexa' in question:
        question = question.replace('Alexa','')
        #print(question)
        if 'what are you doing' in question:
            answer = ('I am waiting for your question')
            talk(answer)

        elif 'how are you' in question:
            answer = ('I am doing good, how are you dear')
            talk(answer)

        elif 'play' in question:
            question = question.replace('play','')
            pywhatkit.playonyt(question)

        elif 'tell me about' in question:
            question = question.replace('tell me about','')
            wiki = wikipedia.summary(question,1)
            print(wiki)
            talk(wiki)

        elif 'time' in question:
            time = datetime.today().time().strftime('%I:%M %p')
            print(time)
            talk(time)

        elif 'joke' in question:
            joke = pyjokes.get_joke()
            print(pyjokes.get_joke())

        elif 'age' in question:
            question = question.replace('age','')
            answer = ('Why do you want my age fuckig bitch')
            talk(answer)

        elif 'what does' in question:
            question = question.replace('what does','')
            answer = ('nani')
            talk(answer)

        elif 'weather' in question:
            question = question.replace('weather','')
            answer = get_weather('london')
            talk(answer)
    else:
        print('Sorry, Are you talking to me?')

except sr.UnknownValueError:
    print ("sorry,I can't get your question")
