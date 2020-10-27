import nltk
from .opinion_unit_divider import opinion_unit_creator

def preprocess_review(review_headline, review_body):
    tmp_review = review_headline + '. ' + review_body

    sentence_tokens = nltk.sent_tokenize(tmp_review)
    opinion_units = opinion_unit_creator(sentence_tokens)

    return opinion_units