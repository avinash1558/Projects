from Speak import Speak
from Listening import Listening
from Name_ import name_
import time

def namechange():
    name1=name_()
    try:
        Speak("Which name do you want?")
        i = 1
        while 1:
            sp=1
            sentence = Listening()
            name = sentence
            if sentence != "none":
                Speak("this name is correct or not")

                j = 1  
                while j <= 2:
                    sentence = Listening()
                    if "yes" in sentence or "correct" in sentence and "no" not in sentence or "right" in sentence or "write" in sentence:
                        with open("Database\\name.txt", "w") as w:
                            w.write(name)
                        with open("Database\\qna_log.txt", "a") as w:
                            w.write(
                                f"\nQuestion : what is you name \nAnswer : My name is {name_()}.")
                        with open("Database\\chat_log.txt", "a") as w:
                            w.write(
                                f"\nYou : what is you name \n{name_().capitalize()} : My name is {name_().capitalize()}.")
                        Speak(f"i am changing my name to {name}")
                        time.sleep(2)
                        return
                    elif "no" in sentence or "wrong" in sentence:
                        Speak("Which name do you want speak again !")
                        time.sleep(2)
                        sp=2
                        break
                    j = j+1
                if sp==1:
                    Speak("You did not say anything that's why i am terminating you command")
                    time.sleep(2)
                    return
    except:
        Speak("An unknown error occurred, Sorry sir try again")
        time.sleep(2)
