# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import urllib.request, json
url = "http://newsapi.org/v2/top-headlines?pageSize=100&language=en&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
response = urllib.request.urlopen(url)
data = {}
with urllib.request.urlopen(url) as u:
    data = json.loads(u.read())

articles = data["articles"]
client = language.LanguageServiceClient()
scores = []
for i in range(len(articles)):
    text = articles[i]['content']
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    try:
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        scores.append(sentiment.score)
    except:
        print("error")
# Instantiates a client
print(scores)


# The text to analyze
# text = "Hidden in the grim data are hints of recovery from the pandemic recession"
# document = types.Document(
#     content=text,
#     type=enums.Document.Type.PLAIN_TEXT)

# # Detects the sentiment of the text
# sentiment = client.analyze_sentiment(document=document).document_sentiment

# print('Text: {}'.format(text))
# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))