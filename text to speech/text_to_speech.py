import pyttsx3
engine = pyttsx3.init()
text = input("enter text in english")
engine.say(text)
engine.runAndWait()
