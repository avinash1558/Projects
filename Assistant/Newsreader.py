import requests
import json
from Speak import Speak
import time
from Listening import Listening


def readnews():
    try:
        with open("DataBase\\ApiNews.txt", "r") as r:
            api = r.read()
        data = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api}").text
        news = json.loads(data)
        newsArticle = news['articles']
        Speak('Now i am reading news')
        i = 0
        for SPEAK in newsArticle:
            if i <= 2:
                Speak("Title : ")
                time.sleep(0.3)
                Speak(SPEAK['title'])
                Speak("Description :")
                time.sleep(0.3)
                Speak(SPEAK['description'])
                time.sleep(1)
                if i <= 1:
                    Speak('Next news :')
            i = i+1

            if i > 3:
                Speak("Do you want more news ")
                j = 0
                while j <= 1:
                    j = j+1
                    sentence = Listening()
                    if "yes" in sentence or "more" in sentence and "no" not in sentence:
                        j = 0
                        while j <= 1:
                            j = j+1
                            Speak('Next news : ')
                            time.sleep(0.5)
                            Speak("Title : ")
                            time.sleep(0.3)
                            Speak(SPEAK['title'])
                            Speak("Description : ")
                            time.sleep(0.3)
                            Speak(SPEAK['description'])
                            time.sleep(1)
                        Speak("thanks for listening")
                        time.sleep(2)
                        return 0
                    if "no" in sentence or "more" in sentence and "yes" not in sentence: 
                        Speak("thanks for listening")
                        time.sleep(2)
                        return 0
                Speak("thanks for listening")
            time.sleep(1)

    except:
        Speak("An unknown error occurred, Sorry sir try again")

        time.sleep(2)
    # Speak('thanks for listening you')
