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

def processQuestion(question):

    if 'what are you doing' in question:
        print("Human:", question)
        answer = ('I am waiting for your question')
        print('Voice Assistant:', answer)
        talk(answer)
        return True

    # This will execute when you ask question How are you
    elif 'how are you' in question:
        print("Human:", question)
        answer = ('I am doing good, how are you dear')
        talk(answer)
        print('Voice Assistant:', answer)
        return True

    # To play songs in youtube just say "play song_name"
    elif 'play' in question:
        print("Human:", question)
        question = question.replace('play', '')
        pywhatkit.playonyt(question)
        return True

    elif 'tell me about' in question:
        print("Human:", question)
        question = question.replace('tell me about', '')
        wiki = wikipedia.summary(question, 1)
        print(wiki)
        talk(wiki)
        return True

    elif 'time' in question:
        print("Human:", question)
        time = datetime.today().time().strftime('%I:%M %p')
        print(time)
        talk(time)
        return True

    elif 'age' in question:
        print("Human:", question)
        # question = question.replace('age', '')
        print("I don't know my age,but I was created on 27/01/2022")
        answer = ("I don't know my age,but I was created on 27/01/2022")
        talk(answer)
        return True

    elif 'who is' in question:
        print("Human:", question)
        question = question.replace('who is', '')
        answer = (question,'is waste fellow')
        talk(answer)
        return True
    elif 'bye' in question:
        print("bye")
        return "bye"
    elif 'weather' in question:
        print("#Human:", question)
        # question = question.replace('weather', '')
        answer = get_weather('london')
        talk(answer)
        return True

    else:
        question = r.recognize_google(audio)
        print("Voice Assistant: sorry,I can't find answer to", question)
        answer = ("sorry,I can't find answer to", question, "Say Again")
        print("Say Again....")
        talk(answer)
        return True

def getQuestion():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        answer = 'You are speaking to AI voice assistant, How can I help!'
        print('Voice Assistant:')
        talk(answer)
        print("listening....")
        audio = r.listen(source)
        try:
            # print(r.recognize_google(audio))
            question = r.recognize_google(audio)
            if 'Alexa' in question:
                question = question.replace('Alexa', '')
                # print(question)
                return question
            else:
                return "nottalkingtome"

        except sr.UnknownValueError:
            print("Since No Response from you, Good bye for now")
            answer = "Since No Response from you, Good bye for now"
            talk(answer)
            return "Unknownvalue"

Askquestion = True

while Askquestion:
    question = getQuestion()
    if (question == "nottalkingtome"):
        talk("Since, you are not talking to me good bye for now")
        Askquestion = False
    elif (question == "Unknownvalue"):
        Askquestion = False
    elif (question == "bye"):
        Askquestion = False
    else:
        Askquestion = processQuestion(question)
