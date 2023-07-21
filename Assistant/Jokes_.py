import random
import pyjokes
import pyttsx3
from gtts import gTTS
import time 
from time import sleep
from playsound import playsound
import os
from Listening import Listening


def SpeakH(str, lang="hi", speed=False):
    """
    its take string and speak that string
    """
    gtt = gTTS(text=str, lang=lang, slow=speed)
    filename = "avn.mp3"
    gtt.save(filename)
    playsound(filename)
    os.remove(filename)
    time.sleep(0.2)


def SpeakE(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(Text)
    engine.runAndWait()


def H_Jokes():
    """
    its provide hindi jokes by static method
    """
    try:
        li = ["पप्पू अपनी पत्नी से-  अच्छा ये बताओ 'बिदाई' के समय तुम  लड़कियां इतनी रोती क्यों हो?   पत्नी- 'पागल' अगर तुझे पता चले...  अपने घर से दूर ले जाकर कोई तुमसे  'बर्तन मंजवाएगा' तो तू  क्या    नाचेगा...", "बैंक की cashier ने खिड़की पर खड़े आदमी को कहा 'पैसे नहीं है'   ग्राहक: और दो मोदी माल्या को पैसा, सारे पैसे लेकर भाग गए विदेश में    कैशियर ने खिड़की में से हाथ निकाला और उसकी गर्दन दबोच कर कहा 'साले बैंक में तो है तेरे खाते में हीं है' भिखारी  ", "    जज : घर में मालिक होते हुए तूने चोरी कैसे की?    चोर : साहब, आपकी नौकरी अच्छी है, और सैलरी     भी अच्छी है, फिर आप ये सब सीख कर क्या करोगे?    ", " पब्लिक टॉयलेट में लिखा था    'दुनिया चांद पर पहुंच गयी और तू यहीं पर बैठा है'    पप्पू ने अपना दिमाग लगाया और नीचे लिखा    'चांद पर पानी नहीं था इसलिए वापस आ गया'    ", "    पति- प्यास लगी है पानी लेके आओ..    पत्नी- क्यों ना आज तुम्हें मटर पनीर     और शाही पुलाव बनाकर लाऊं...    पति- वाह वाह...!    मुंह में पानी आ गया..    पत्नी- आ गया ना मुंह में पानी   बस इसी से काम चला लो..    ", "  टीचर- टिटू बताओ..   अकबर ने कब तक शासन किया था ?   टिटू- सर जी..   पेज नंबर 14 से लेकर पेज नंबर 22 तक..।    ",
              "    गोलू- जानू, तुम दिन पर दिन    खूबसूरत होती जा रही हो...    पत्नी (खुश होकर)- तुमने कैसे जाना ?    गोलू- तुम्हें देखकर...    रोटियां भी जलने लगी हैं   ", "टिल्लू (लड़की से)- मैं 18 साल का हूं   और तुम ?    लड़की- मैं भी 18 साल की हूं...   टिल्लू- तो फिर चलो ना, इसमें शरमाना क्या..    लड़की- कहां ?    टिल्लू- अरे पगली..    वोट देने और कहां..", "    मां- बेटा क्या कर रहे हो    पप्पू- पढ़ रहा हूं मां..    - शाबास! बेटा क्या पढ़ रहे हो..?    पप्पू- आपकी होने वाली बहु के SMS", "    टीचर- बच्चों कोई ऐसा वाक्य सुनाओ     जिसमें हिंदी, पंजाबी, उर्दू और अंग्रेजी का प्रयोग हो..    पप्पू- सर ..    'इश्क दी गली विच ल No entry'", "    पत्नी- पूजा किया कीजिए,    बड़ी बलांए टल जाती हैं...    टिटू- हां... तुम्हारे    पिताजी ने बहुत की होगी     उनकी टल गई और मेरे पल्ले पड़ गई..।", "  जिस तरह अच्छी हवा, अच्छा   खानपान किसी भी इंसान के सेहतमंद रहने के लिए जरूरी होता है, उसी   प्रकार आपकी हंसी भी आपको स्वस्थ रखने में अहम भूमिका निभाती है। अगर   आप सुबह-शाम हंसने की आदत डाल लें तो कोई भी बीमारी, चाहे मानसिक हो या  शारीरिक आपके पास भी नहीं आएगी। इसीलिए हम आपके लिए कुछ ऐसे मजेदार  चुटकुले लेकर आए हैं, जिन्हें पढ़ने के बाद आप हंसते-हंसते लोटपोट हो    जाएंगे। तो चलिए शुरू करते हैं हंसने-हंसाने का ये सिलसिला...", "पापा- तेरा रिजल्ट आ गया, पास हुआ या फेल?    चिंटू- प्रिंसिपल का बेटा फेल हो गया    पापा- तुम?    चिंटू- मेजर साहब का बेटा भी फेल हो गया     पापा- और तुम?    चिंटू- डॉक्टर साहब का बेटा भी फेल हो गया   पापा गुस्से से- बेवकूफ, मैं तुमसे पूछ रहा हूं तुम्हारे रिजल्ट का क्या हुआ?   चिंटू -तो आप कौन से प्रधानमंत्री हो जो आपका बेटा पास हो जाएगा...", "टीचर- एक औरत एक घंटे मे 50 रोटी बना लेती है, तो तीन औरतें एक घंटे में कितनी रोटी बनाएंगी.. .बच्चा- एक भी नही, क्योंकि तीनों मिलकर सिर्फ चुगली करेंगी...! .बच्चे की बात सुनकर टीचर अभी तक बेहोश है...", "पप्पू जलेबी बेच रहा था, लेकिन कह रहा था  आलू ले लो आलू ले लो... राहगीर- लेकिन ये तो जलेबी है   .पप्पू- चुप हो जा! वरना मक्खियां आ जाएंगी।", "वकील - हत्या की रात तुम्हारे पति के अंतिम शब्द?  .पत्नी - मेरा चश्मा कहां है संगीता...?        .वकील - तो इसमें मारने वाली क्या बात थी...?.   पत्नी - मेरा नाम रंजना है!   .पूरा कोर्ट खामोश...", "एक सज्जन बता रहे थे कि वो पिछले 20 सालों से गीता के उपदेश सुनते आ रहे हैं...!  पता करने पर पता चला कि  गीता उनकी धर्मपत्नी का नाम है...!!!", "मास्टर जी - शांति किसके घर में रहती है...? पप्पू - जिस घर में पति और पत्नी दोनों मोबाइल चलाते हैं...!!!"]
        joketext = random.choice(li)
        SpeakH(joketext)
        # SpeakH("har")
        time.sleep(1)
        SpeakE("Do you want again ")
        i = 1
        while i <= 2:
            i = i+1
            sentence = Listening()
            if "yes" in sentence:
                joketext = random.choice(li)
                SpeakH(joketext)
                SpeakH("thanks for listening")
                sleep(2)
            if "no" in sentence:
                SpeakH("thanks for listening")
                sleep(2)
                return
    except Exception as e:
        SpeakE("Sorry for inconvenient , Try again")


def E_Jokes(j_lan='en'):
    '''
        its give jokes dynamicly
        category: str
        Choices: 'neutral', 'chuck', 'all', 'twister'
        lang: str
        Choices: 'en', 'de', 'es', 'gl', 'eu', 'it'
    '''
    try:
        Choices = ['neutral', 'chuck', 'all', 'twister']
        MyJoke = pyjokes.get_joke(language=j_lan, category="all")
        SpeakE(MyJoke)
        time.sleep(1)
        SpeakE("Do you want again ")
        i = 1
        while i <= 2:
            i = i+1
            sentence = Listening()
            if "yes" in sentence:
                MyJoke = pyjokes.get_joke(language=j_lan, category="all")
                SpeakE(MyJoke)
                SpeakE("thanks for listening")
                sleep(2)
            if "no" in sentence:
                SpeakE("thanks for listening")
                sleep(2)
                return
    except Exception as e:
        SpeakE("Sorry for inconvenient , Try again")

# H_Jokes()