import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

EMAIL = "bkashishh07@gmail.com"
# PASSWORD ="trywlbpzchnmglzu"
PASSWORD = " kmlamdibgonscago"



# def find_my_ip():
#     ip_adress = requests.get('https://api.ipify.org?format=json').json()
#     return ip_adress['ip']

def find_my_ip():
    # Make a GET request to the IPify API to retrieve the public IP address
    response = requests.get('https://api.ipify.org?format=json')

    # Convert the JSON response to a Python dictionary
    ip_address_data = response.json()

    # Extract and return the IP address from the response
    ip_address = ip_address_data['ip']
    return ip_address

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)

import smtplib
from email.message import EmailMessage

def send_email(receiver_add, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_add
        email['Subject'] = subject
        email['From'] = EMAIL

        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True

    except Exception as e:
        print(e)
        return False





def get_news():
    news_headline = []

    result = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2024-02-24&sortBy=publishedAt&apiKey=f8f4d78e76d545abb872decfc3241585").json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]



def weather_forecast(city):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=72c91e08af9d61fddd886e66dfa324e0"
                       ).json()
    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temp}°C", f"{feels_like}°C"

