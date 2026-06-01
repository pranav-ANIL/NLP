import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
r = sr.Recognizer()
translator = Translator()
with sr.Microphone() as source:
    print("please speak")
    try:
        audio = r.listen(source,timeout=7)
        text = r.recognize_google(audio)
        print("you said:",text)
        translated=translator.translate(text,src="en",dest="hi")
        print(translated.text)
        tts = gTTS(text=translated.text, lang="hi")
        tts.save("hindi_output.mp3")
        os.system("start hindi_output.mp3")
    except sr.WaitTimeoutError:
        print("you did not speak.please speak")
    except sr.UnknownValueError:
        print("i heard something,but could not understand.please speak clearly")