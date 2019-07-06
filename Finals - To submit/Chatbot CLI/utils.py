import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return "Normal"

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def read_corpus():
    fp = open('data.txt', "r+")
    raw = fp.read()
    raw = raw.lower()
    sent_tokens = raw.splitlines(True)
    # print(sent_tokens)
    ques_sent_tokens = []
    ans_sent_tokens = []
    for i in sent_tokens:
        ques, ans = i.split("-x-")
        ques_sent_tokens.append(ques)
        ans_sent_tokens.append(ans)
    return ques_sent_tokens,ans_sent_tokens

def write_corpus(ques_sent_tokens, ans_sent_tokens):
    for i in range(len(ques_sent_tokens)):
        ques_sent_tokens[i] = ques_sent_tokens[i] + " -x- " + ans_sent_tokens[i]
    fp = open('data.txt', "r+")
    fp.seek(0,0)
    fp.writelines(ques_sent_tokens)
    fp.close()

def response(user_response,ques_sent_tokens,ans_sent_tokens):
    user_response = nltk.sent_tokenize(user_response)
    chatty_response=''
    qst = list(ques_sent_tokens)
    qst.append(user_response[0])
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidfVec.fit_transform(qst)
    vals = cosine_similarity(tfidf[-1], tfidf)
    # print(vals)
    # print(vals.argsort())
    # print(ans_sent_tokens)
    idx=vals.argsort()[0][-2]
    if(vals[0][idx]<0.5):
        chatty_response=chatty_response+"I am sorry! I don't understand you"
        return chatty_response, False
    else:
        chatty_response = chatty_response+ans_sent_tokens[idx]
        return chatty_response, True