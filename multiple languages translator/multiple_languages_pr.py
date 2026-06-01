import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
r = sr.Recognizer()
translator = Translator()
languages = {"1":("Hindi","hi"),"2":("Malayalam","ml"),"3":("Tamil","ta")
             ,"4":("Telugu","te"),'5':("French","fr"),"6":("Spanish",'es')}
print("choose your desired language")
for key,(name,_) in languages.items():
    print(f"{key}.{name}")
choice = int(input("enter a number:"))
lang_name, lang_code = languages.get(choice, (name,_))
print(f"Translating to {lang_name}...")
with sr.Microphone() as source:
    print("please speak")
    try:
        audio = r.listen(source,timeout=7)
        text = r.recognize_google(audio)
        print("you said:",text)
        translated=translator.translate(text,src="en",dest=lang_code)
        print(translated.text)
        tts = gTTS(text=translated.text, lang=lang_code)
        tts.save("output.mp3")
        os.system("start output.mp3")
    except sr.WaitTimeoutError:
        print("you did not speak.please speak")
    except sr.UnknownValueError:
        print("i heard something,but could not understand.please speak clearly")