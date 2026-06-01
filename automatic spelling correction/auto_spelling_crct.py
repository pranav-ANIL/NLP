from textblob import TextBlob 
text = input("Enter your text:")
blob = TextBlob(text)
corrected = blob.correct()
print("your org text:",text)
print("your corrected  text:",corrected)