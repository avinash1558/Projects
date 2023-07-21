from Speak import Speak
from pywikihow import search_wikihow
from time import sleep

def howto(str):
    try:
        data = str.split("how to ")[1]
        max_r = 1
        how_to = search_wikihow(data, max_r)
        assert len(how_to) == 1
        Speak(how_to[0].summary)
        sleep(2)

    except:
        Speak("An unknown error occurred, Sorry sir try again")
        sleep(2)
# howto("how to download app in google")

