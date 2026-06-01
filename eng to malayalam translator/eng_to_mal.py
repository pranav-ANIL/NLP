from googletrans import Translator
translator = Translator()
text = input("enter text in english:")
translated=translator.translate(text,dest="ml")
print("malayalam:",translated.text)