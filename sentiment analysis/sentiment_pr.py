from textblob import TextBlob
text = input("Enter your review: ")
blob=TextBlob(text)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity
if polarity>0:
    sentiment= "positive"
elif polarity<0:
    sentiment= "negative"
else:
    sentiment="neutral"
print(f"Sentiment:    {sentiment}")
print(f"Polarity:     {polarity:.2f}  (-1 = very negative, +1 = very positive)")
print(f"Subjectivity: {subjectivity:.2f}  (0 = factual, 1 = very opinionated)")