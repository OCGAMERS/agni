import pyttsx3
import speech_recognition 
import os
import datetime
import random
import pygame
from pygame import mixer
import speedtest
from plyer import notification
import requests
from bs4 import BeautifulSoup
import pyautogui
import serial
import time

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


for i in range(3):
    speak("Enter Password to open Agni ")
    a = takeCommand()
    pw_file = open("password.txt","r")
    pw = pw_file.read().strip()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        speak("Incorrect password. Exiting")
        exit()

    elif (a!=pw):
        print("Incorrect password. Try Again")

from INTRO import play_intro

try:
    bluetooth_port = 'COM9'
    baud_rate = 9600
    ser = serial.Serial(bluetooth_port, baud_rate)
    speak(f"Connected to {bluetooth_port} at {baud_rate} baud rate.")
except :
    speak("Not Connected to bluetooth")
def send_command(command):
    ser.write(command.encode())
    print(f"Sent command: {command}")

greetings = {
    "hello": "Hello, how are you?",
    "hi": "Hi there!",
    "hey": "Hey, how's it going?",
    "greetings": "Greetings, sir.",
    "good day": "Good day! How can I assist you today?",
    "howdy": "Howdy! What can I do for you?",
    "what's up": "Hey, what's up?",
    "nice to see you": "Nice to see you! How have you been?",
    "how's everything": "How's everything going?",
    "how are you today": "I'm great, thanks! How about you?",
    "good to see you": "Good to see you too!",
    "hey there": "Hey there! What's new?",
    "how's your day": "How's your day going?",
    "great to see you": "Great to see you! How can I assist you?",
    "pleased to meet you": "Pleased to meet you! How can I help?",
    "how have you been": "I've been good, thank you!",
    "nice seeing you": "Nice seeing you too! What's up?",
    "good to hear from you": "Good to hear from you! How's it going?",
    "long time no see": "Long time no see! What's new?",
    "good evening": "Good evening! How may I assist you?",
    "hey buddy": "Hey buddy! How's your day been?",
    "good to see you again": "Good to see you again! How can I help you?",
    "how's everything going": "How's everything going for you?",
    "it's good to see you": "It's good to see you! How are you doing?",
    "hey friend": "Hey friend! What's up?",
    "hey mate": "Hey mate! How have you been?",
    "nice to meet you": "Nice to meet you! How's your day?",
    "it's nice to see you": "It's nice to see you! What's new?",
    "hey there buddy": "Hey there buddy! How's everything?",
    "it's great to see you": "It's great to see you! How's your day going?",
    "hey dude": "Hey dude! What's going on?",
    "how's everything been": "How's everything been for you?",
    "it's good to hear from you": "It's good to hear from you! How are things?",
    "good afternoon": "Good afternoon! How's your day going?",
    "hello there": "Hello there! How can I assist you today?",
    "how have you been lately": "How have you been lately? What's new?",
    "nice to see you again": "Nice to see you again! How can I help?",
    "it's great to hear from you": "It's great to hear from you! How are things?",
    "hey there friend": "Hey there friend! How's everything going?",
    "it's good to see you again": "It's good to see you again! How's everything?",
    "hey there mate": "Hey there mate! How's your day been?",
    "how's everything with you": "How's everything with you? What's new?",
    "hey there buddy": "Hey there buddy! How's everything going?",
    "good to hear from you again": "Good to hear from you again! How are things?",
    "hey there dude": "Hey there dude! What's going on?",
    "nice to see you today": "Nice to see you today! How's everything?",
    "hey there friend": "Hey there friend! How's your day been?",
    "it's nice to hear from you": "It's nice to hear from you! How are things?",
    "hello again": "Hello again! How's your day going?",
    "it's nice to see you again": "It's nice to see you again! What's new?",
}

number_map = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10
        }

def schedule_my_day():
    tasks = []
    speak("Do you want to clear old tasks? Please say YES or NO.")
    query = takeCommand().lower()

    if query and "yes" in query:
        with open("tasks_file", "w") as file:
            file.write("")
        speak("Tasks cleared. How many tasks do you want to add?")
        n = takeCommand().lower()

        no_tasks = number_map.get(n, 3)  # Default to 3 tasks if input not in the dictionary

        for i in range(no_tasks):
            speak(f"Enter task {i + 1}:")
            task = takeCommand()
            tasks.append(task)
            with open("tasks_file", "a") as file:
                file.write(f"{i + 1}. {task}\n")
    elif "no" in query:
        speak("How many tasks do you want to add?")
        n = takeCommand().lower()

        no_tasks = number_map.get(n, 3)  # Default to 3 tasks if input not in the dictionary

        for i in range(no_tasks):
            speak(f"Enter task {i + 1}:")
            task = takeCommand()
            tasks.append(task)
            with open("tasks_file", "a") as file:
                file.write(f"{i + 1}. {task}\n")
    speak("Tasks scheduled successfully.")
def show_my_schedule():
    try:
        with open("tasks_file", "r") as file:
            content = file.read()
            speak("Your schedule is as follows.")
            speak(content)
            mixer.init()
            mixer.music.load("notification.mp3")
            mixer.music.play()
            notification.notify(
                title="My schedule",
                message=content,
                timeout=15
            )
            speak("Your schedule has been shown.")
            
            # Ask if the user wants to view the schedule again
            speak("Do you want to view the schedule again? Please say YES or NO.")
            query = takeCommand().lower()
            if query and "yes" in query:
                show_my_schedule()
    except FileNotFoundError:
        speak("No tasks scheduled.")


def greet():
    from Greet_Me import greetMe
    greetMe()

def get_weather():
    try:
        search = "temperature in hyderabad"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"Current {search} is {temp}")
    except Exception as e:
        speak("Sorry, I couldn't fetch the weather details.")

def search_google(query):
    try:
        from Search_Now import searchGoogle
        searchGoogle(query)
    except Exception as e:
        speak("Sorry, I couldn't perform the Google search.")

def get_time():
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"Sir, the time is {strTime}")

def set_alarm(time):
    alarm(time)
    speak("Alarm set for " + time)

pygame.mixer.init()
paused = False
volume = 1  # Volume is from 0.0 to 1.0

def play_song(folder_path):
    try:
        global paused
        songs = os.listdir(folder_path)
        songs = [song for song in songs if song.endswith('.mp3')]
        if not songs:
            speak("There are no songs in the specified folder.")
            return

        selected_song = random.choice(songs)
        song_path = os.path.join(folder_path, selected_song)

        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        paused = False
        speak(f"Playing {selected_song}")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't play the song.")

def pause_song():
    global paused
    try:
        if pygame.mixer.music.get_busy() and not paused:
            pygame.mixer.music.pause()
            paused = True
            speak("Song paused.")
        elif paused:
            speak("The song is already paused.")
        else:
            speak("No song is currently playing.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't pause the song.")

def unpause_song():
    global paused
    try:
        if paused:
            pygame.mixer.music.unpause()
            paused = False
            speak("Song resumed.")
        else:
            speak("No song is currently paused.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't resume the song.")

def stop_song():
    global paused
    try:
        if pygame.mixer.music.get_busy() or paused:
            pygame.mixer.music.stop()
            paused = False
            speak("Song stopped.")
        else:
            speak("No song is currently playing.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't stop the song.")

def mute_song():
    global volume
    try:
        if pygame.mixer.music.get_busy() or paused:
            pygame.mixer.music.set_volume(0)
            volume = 0
            speak("Song muted.")
        else:
            speak("No song is currently playing.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't mute the song.")

def unmute_song():
    global volume
    try:
        if pygame.mixer.music.get_busy() or paused:
            pygame.mixer.music.set_volume(1)
            volume = 1
            speak("Song unmuted.")
        else:
            speak("No song is currently playing.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't unmute the song.")

recipient_mapping = {
    "ram": "satyasriramsriram435@gmail.com",
    "madhav": "22r21a3319@mlrit.ac.in",
    "rahul": "22r21a3304@mlrit.ac.in",
    "santhosh": "22r21a3332@mlrit.ac.in"
}

sender_choices = {
    'first': ("satyasriramsriram435@gmail.com", "gvpg wwjd dwpr watp"),
    'second': ("nishchayreddy03@gmail.com", "ormj sfph kwpv dlsi")
}

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

songs_folder=r'C:\Users\HP\Desktop\SAMPLE\songs'


if __name__ == "__main__":
  while True:
    query = takeCommand().lower()
    if "wake up" in query:
     from Greet_Me import greetMe
     greetMe()

     while True:
        query = takeCommand().lower()
        if "go to sleep" in query:  #############################################
            speak("Ok sir , You can call me anytime")
            break 
        for key in greetings:
            if key in query:
                speak(greetings[key])
                break

        if "wikipedia" in query:    ##############################################
            from Search_Now import searchWikipedia
            searchWikipedia(query)

        elif "google" in query:     #################################################
            search_google(query)

        elif "temperature" in query:    ################################################
            get_weather()

        elif "the time" in query:   ###################################################
            get_time()

        elif "stop listening" in query: ###############################################
            speak("stopped listening ,sir")
            exit()

        elif "set an alarm" in query:   ####################################################
            speak("Please tell the time for the alarm. For example, say ten fifteen AM.")
            time = takeCommand()
            alarm(time)
            speak("Alarm set successfully, sir.")

        elif "volume up" in query:     ###################################################
            from keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()

        elif "volume down" in query:    ###################################################
            from keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()

        elif "remember that" in query:  ####################################################
                rememberMessage = query.replace("remember that", "")
                rememberMessage = rememberMessage.replace("jarvis", "")
                speak("You told me to " + rememberMessage)
                with open("Remember.txt", "a") as remember:
                    remember.write(rememberMessage + "\n")

        elif "what do you remember" in query:   ################################################
            with open("Remember.txt", "r") as remember:
                content = remember.read()
                if content:
                    speak("You told me to " + content)
                else:
                    speak("I do not have any specific information to remember.")

        elif "forget what you remember" in query:   ############################################
                with open("Remember.txt", "w") as remember:
                    remember.write("")
                speak("I have forgotten what you asked me to remember.")

        elif "tired" in query:
            speak("Playing your favourite songs, sir")
            play_song(songs_folder)

        elif "pause" in query:
            pause_song()

        elif "play" in query or "resume" in query:
            unpause_song()

        elif "stop" in query:
            stop_song()

        elif "mute" in query:
            mute_song()

        elif "unmute" in query:
            unmute_song()
        
        elif "news" in query:   #######################################################
            from News_read import latestnews
            latestnews()
        
        elif "change password" in query:    ##################################################
            speak("What's the new password?")
            new_pw = takeCommand().lower()  # Assuming takeCommand() retrieves voice input
            if new_pw:
                with open("password.txt", "w") as new_password:
                    new_password.write(new_pw)
                speak("Password changed successfully.")
                speak(f"Your new password is {new_pw}")
            else:
                speak("Password change failed. Please try again.")

        elif "schedule my day" in query:    #####################################################
            schedule_my_day()

        elif "show my schedule" in query:   #####################################################
            show_my_schedule()

        elif "open" in query:   #EASY METHOD
            query = query.replace("open","")
            query = query.replace("jarvis","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter") 

        elif "internet speed" in query:
            wifi = speedtest.Speedtest()
            wifi.get_best_server()
            # Calculate download speed
            download_speed = wifi.download() / 1_000_000  # in Megabits per second
            # Calculate upload speed
            upload_speed = wifi.upload() / 1_000_000  # in Megabits per second
            speak(f"Wifi download speed is {download_speed:.2f} Mbps.")
            speak(f"Wifi upload speed is {upload_speed:.2f} Mbps.")

        elif "translate" in query:
            from translator import translategl
            query = query.replace("jarvis","")
            query = query.replace("translate","")
            translategl(query)

        elif "light on" in query:   ##########################################################
            send_command('1')
            speak("Light On")

        elif "light off" in query:  ###########################################################
            send_command('0')
            speak("Light Off")

        elif "send email" in query:
            try:
                speak("Which sender email do you want to use? ( first or second)")
                sender_choice = takeCommand().strip()
                from send_email import send_email
                if sender_choice in sender_choices:
                    sender_email, sender_password = sender_choices[sender_choice]
                    speak("To whom do you want to send the email")
                    for username, email in recipient_mapping.items():
                        speak(f"Username: {username}")

                    recipient_name = takeCommand().lower()
                    recipient_email = recipient_mapping.get(recipient_name)

                    if recipient_email:
                        speak("What is the subject of the email?")
                        subject = takeCommand().lower()

                        speak("What is the message of the email?")
                        content = takeCommand().lower()
                        
                        send_email(sender_email, sender_password, recipient_email, subject, content)

                    else:
                        speak("Sorry! I am not able to find the recipient's email address")
                else:
                    speak("Invalid choice for sender email")
            except Exception as e:
                speak(f"An error occurred: {str(e)}")

ser.close()
print("Serial connection closed.")