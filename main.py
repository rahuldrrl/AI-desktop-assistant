import pyttsx3
import speech_recognition as sr
import keyboard
import os
import subprocess as sp
import imdb
import webbrowser
import wolframalpha
from decouple import config
from datetime import datetime
from random import choice
from conv import random_text
from online import find_my_ip, search_on_google, search_on_wikipedia, youtube, send_email, get_news, weather_forecast
from virtualmouse import virtual_mouse_control
import threading
from volumetest import hand_gesture_control
import time
from intro import play_gif
from head import  eye_control_mouse
play_gif()
engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 225)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
USER = config('USER')
HOSTNAME = config("BOT")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.now().hour
    if hour < 12:
        speak(f"Good morning, {USER}")
    elif hour < 17:
        speak(f"Good afternoon, {USER}")
    elif hour < 19:
        speak(f"Good evening, {USER}")
    else:
        speak(f"hi , {USER}")
    speak(f"I am {HOSTNAME}. How may I assist you, {USER}?")


listening = False


def start_listening():
    global listening
    listening = True
    print(" start listening ..  ")


def pause_listening():
    global listening
    listening = False
    print("stopped listening..")


keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good Night sir ,take care ")
            else:
                speak("Have a Good day sir !")
            exit()

    except Exception:
        speak("Sorry i cauld not understand . Can you please repeat that ?")
        queri = 'None'
    return queri


if __name__ == '__main__':
    greet_me()

    while True:
        if listening:
            query = take_command().lower()
            if "how are you " in query:
                speak("I am absolutely fine sir ,what about you ")
            elif "open command prompt" in query:
                speak("Opening command prompt")
                os.system('start cmd')
            elif "open camera" in query:
                speak("Opening camera sir ")
                webbrowser.open("microsoft.windows.camera://")
                os.startfile("microsoft.windows.camera://")


            elif "open notepad" in query:
                speak("Opening Notepad for you sir ")
                notepad_path = "C:\\Windows\\notepad.exe"
                os.startfile(notepad_path)
                time.sleep(3)
            elif "open discord" in query:
                speak("Opening Discord sir")
                # discord_path="C:\Users\ASHISH\AppData\Roaming\discord"
                discord_path = "C:\\Users\\ASHISH\\AppData\\Roaming\\discord"

                os.startfile(discord_path)

            elif "find my adress " in query:
                speak("Finding IP address for you.")
                ip_address = find_my_ip()
                speak(f"Your IP address is {ip_address}")
                print(f"Your IP address is {ip_address}")


            elif "open youtube" in query:
                speak("What do you want to play on YouTube, sir?")
                video = take_command().lower()
                youtube(video)
                time.sleep(7)


            elif "open google" in query:
                speak(f"what do you want to search on google {USER}")
                query = take_command().lower()
                search_on_google(query)

            elif "wikipedia" in query:
                speak("what do you want to search on wikipedia sir")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f" According to wikipedia ,{results}")
                speak(" I am printing in on terminal")
                print(results)



            elif "send an email" in query:
                speak("On what email address do you want to send sir?. Please enter in the terminal")
                receiver_add = input("Email address:")
                speak("What should be the subject sir?")
                subject = take_command().capitalize()
                speak("What is the message ?")
                message = take_command().capitalize()

                if send_email(receiver_add, subject, message):
                    speak("I have sent the email sir")
                    print("I have sent the email sir")
                else:
                    speak("something went wrong Please check the error log")

            elif "give me news" in query:
                speak(f"I am reading out the latest headline of today,sir")
                speak(get_news())
                speak("I am printing it on screen sir")
                print(*get_news(), sep='\n')




            elif "virtual mouse" in query:

                eye_control_thread = threading.Thread(target=eye_control_mouse)
                eye_control_thread.start()
            elif "volume" in query:
                gesture_thread = threading.Thread(target=hand_gesture_control)
                gesture_thread.start()
                time.sleep(15)


            elif 'weather' in query:
                ip_address = find_my_ip()
                speak("tell me the name of your city")
                city = input("Enter name of your city")
                speak(f"Getting weather report for your city {city}")
                weather, temp, feels_like = weather_forecast(city)
                speak(f"The current temperature is {temp}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")



            elif "movie" in query:
                movies_db = imdb.IMDb()
                speak("Please tell me the movie name:")
                text = take_command()
                movies = movies_db.search_movie(text)
                speak("searching for" + text)
                speak("I found these")
                for movie in movies:
                    title = movie["title"]
                    year = movie["year"]
                    speak(f"{title}-{year}")
                    info = movie.getID()
                    movie_info = movies_db.get_movie(info)
                    rating = movie_info["rating"]
                    cast = movie_info["cast"]
                    actor = cast[0:5]
                    plot = movie_info.get('plot outline', 'plot summary not available')
                    speak(f"{title} was released in {year} has imdb ratings of {rating}.It has a cast of {actor}. "
                          f"The plot summary of movie is {plot}")

                    print(f"{title} was released in {year} has imdb ratings of {rating}.\n It has a cast of {actor}. \n"
                          f"The plot summary of movie is {plot}")





            elif "calculate" in query:
                app_id = "XT3G25-LYVEYG3H9T"
                client = wolframalpha.Client(app_id)
                ind = query.lower().split().index("calculate")
                text = query.split()[ind + 1:]
                result = client.query(" ".join(text))
                try:
                    ans = next(result.results).text
                    speak("The answer is " + ans)
                    print("The answer is " + ans)
                except StopIteration:
                    speak("I couldn't find that . Please try again")


            elif 'what is' in query or 'who is' in query or 'which is' in query:
                app_id = "XT3G25-LYVEYG3H9T"
                client = wolframalpha.Client(app_id)
                try:

                    ind = query.lower().index('what is') if 'what is' in query.lower() else \
                        query.lower().index('who is') if 'who is' in query.lower() else \
                            query.lower().index('which is') if 'which is' in query.lower() else None

                    if ind is not None:
                        text = query.split()[ind + 2:]
                        res = client.query(" ".join(text))
                        ans = next(res.results).text
                        speak("The answer is " + ans)
                        print("The answer is " + ans)
                    else:
                        speak("I couldn't find that. Please try again.")
                except StopIteration:
                    speak("I couldn't find that. Please try again.")
