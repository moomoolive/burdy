import nltk
from .opinion_unit_divider import opinion_unit_creator

headline = 'Hi hi'

text = (
    "I love to eat Icecream BUT it's sour. yes, yes! I still eat it although "
    "it's still sour bro. Please leave me alone except for you - you're nice."
)

sent_token = nltk.sent_tokenize(text)
test_token = opinion_unit_creator(sent_token)

def preprocess_review(review_headline, review_body):
    tmp_review = review_headline + '. ' + review_body

    sentence_tokens = nltk.sent_tokenize(tmp_review)
    opinion_units = opinion_unit_creator(sentence_tokens)

    return opinion_units

print(preprocess_review(review_body=text, review_headline=headline))