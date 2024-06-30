import requests
import json
import pyttsx3
import speech_recognition 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=57ffcbe4a4fb43178bf107ba0deb5d48",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=57ffcbe4a4fb43178bf107ba0deb5d48",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=57ffcbe4a4fb43178bf107ba0deb5d48",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=57ffcbe4a4fb43178bf107ba0deb5d48",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=57ffcbe4a4fb43178bf107ba0deb5d48",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=57ffcbe4a4fb43178bf107ba0deb5d48"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = takeCommand()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        speak("Do you want to continue listening ? Please say YES or NO.")
        a = takeCommand()
        if a == "YES":
            pass
        else :
            break
        
    speak("thats all")