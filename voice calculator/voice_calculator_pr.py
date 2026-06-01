import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
engine = pyttsx3.init()
r = sr.Recognizer()
def parse(text):
    text = text.lower()
    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("times", "*")
    text = text.replace("multiplied by", "*")
    text = text.replace("divided by", "/")
    text = text.replace("what is", "")
    text = text.replace(" x ", " * ")
    text = text.replace("calculate", "")
    return text.strip()
with sr.Microphone() as source:
    print("please speak")
    try:
        audio = r.listen(source,timeout=7)
        text = r.recognize_google(audio)
        print("you said:",text)
        expression = parse(text)
        result = eval(expression)
        print("Answer:",result)
        engine.say(f"The answer is,{result}")
    except sr.WaitTimeoutError:
            print("No input detected. Try again.")
    except sr.UnknownValueError:
            print("Could not understand. Please speak clearly.")
   
          