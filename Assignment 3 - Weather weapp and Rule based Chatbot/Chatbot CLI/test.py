import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import utils

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

st = ['what is your name in real life?', 'what do you do for a living?', 'how do you do your job properly?', 'what are you planning to do in summer?']
match = 'how do you manage to do your job properly?'
st.append(match)
TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
tfidf = TfidfVec.fit_transform(st)
vals = cosine_similarity(tfidf[-1], tfidf)
idx=vals.argsort()[0][-2]
print(vals)
print(vals.argsort())
print(idx,st[idx])