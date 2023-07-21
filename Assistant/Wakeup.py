import speech_recognition as sp
from Workinggui import runner
from Name_ import name_

def Listening():
    recgnizeword = ""
    r = sp.Recognizer()
    with sp.Microphone() as source:
        audio = r.listen(source, 0, 3)
    try:
        lis_word = r.recognize_google(audio, language='en-in')
        recgnizeword = str(lis_word).lower()
    except Exception as e:
        recgnizeword = "none"
    return recgnizeword

def WakeupDetected():
    while True:
        sentence = Listening()
        if "wake" in sentence and ("babu" in sentence or name_().lower() in sentence) or "awake up" in sentence and ("babu" in sentence or name_().lower() in sentence) or "hello" in sentence and ("babu" in sentence or name_().lower() in sentence) or "ready" in sentence and ("babu" in sentence or name_().lower() in sentence) or "ok" in sentence and ("babu" in sentence or name_().lower() in sentence):
            runner()
          
WakeupDetected()
