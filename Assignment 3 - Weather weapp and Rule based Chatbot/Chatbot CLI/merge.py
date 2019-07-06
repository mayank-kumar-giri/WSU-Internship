# import nltk
#
# fp = open('data.txt',"r+")
# fp.seek(0,0)
# raw = fp.read().splitlines(True)
# for i in range(len(raw)):
#     print(raw[i].split("-x-"))
# # fp.writelines(final)
# fp.close()
import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
'This is the first document putting synchronization.',
'This document is the second document binding.',
'And this is the third one went.',
 'Is this the first document did?',
]

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

vectorizer = TfidfVectorizer(tokenizer=LemNormalize,analyzer='word')
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X,X.shape)