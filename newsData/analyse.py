from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


client = language.LanguageServiceClient()


def score(text):
    scores = []
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    try:
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        return sentiment.score
    except:
        print("error")