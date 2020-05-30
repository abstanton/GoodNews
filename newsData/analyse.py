from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


client = language.LanguageServiceClient()


# give text from argument a sentiment score between -1 and 1
def score(text):
    scores = []
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    try:
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        return sentiment.score
    except:
        print("analyse.py score error")