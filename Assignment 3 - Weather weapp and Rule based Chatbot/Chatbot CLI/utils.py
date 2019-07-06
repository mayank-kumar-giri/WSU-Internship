import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

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
    # raw = raw.lower()
    sent_tokens = raw.splitlines(True)
    # print(sent_tokens)
    ques_sent_tokens = []
    ans_sent_tokens = []
    for i in sent_tokens:
        ques, ans = i.split("-x-")
        ques_sent_tokens.append(ques.lower())
        ans_sent_tokens.append(ans)
    return ques_sent_tokens,ans_sent_tokens

def write_corpus(ques_sent_tokens, ans_sent_tokens):
    for i in range(len(ques_sent_tokens)):
        ques_sent_tokens[i] = ques_sent_tokens[i] + " -x- " + ans_sent_tokens[i]
    fp = open('data.txt', "r+")
    fp.seek(0,0)
    fp.writelines(ques_sent_tokens)
    fp.close()

def lemmatized_sentences(orig_ques_sent_tokens, orig_ans_sent_tokens):
    ques_sent_tokens = []
    ans_sent_tokens = []
    lemmatizer = WordNetLemmatizer()
    for i in range(len(orig_ques_sent_tokens)):
        qsinit = word_tokenize(orig_ques_sent_tokens[i])
        qsfinal = lemmatizer.lemmatize(qsinit[0])
        for word in qsinit[1:]:
            qsfinal += (" " + lemmatizer.lemmatize(word))
        ansinit = word_tokenize(orig_ans_sent_tokens[i])
        ansfinal = lemmatizer.lemmatize(ansinit[0])
        for word in ansinit[1:]:
            ansfinal += (" " + lemmatizer.lemmatize(word))
        ques_sent_tokens.append(qsfinal)
        ans_sent_tokens.append(ansfinal)
    return ques_sent_tokens,ans_sent_tokens

def response(user_response,ques_sent_tokens,orig_ans_sent_tokens):
    lemmatizer = WordNetLemmatizer()
    urinit = word_tokenize(user_response)
    urfinal = lemmatizer.lemmatize(urinit[0])
    for word in urinit[1:]:
        urfinal += (" " + lemmatizer.lemmatize(word))
    chatty_response=''
    qst = list(ques_sent_tokens)
    qst.append(urfinal)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidfVec.fit_transform(qst)
    vals = cosine_similarity(tfidf[-1], tfidf)
    # print(vals)
    # print(vals.argsort())
    # print(orig_ans_sent_tokens)
    idx=vals.argsort()[0][-2]
    if(vals[0][idx]<0.5):
        if len(urinit) <= 2:
            chatty_response = chatty_response + "Can you please elaborate!"
            return chatty_response, True
        chatty_response = chatty_response+"I am sorry! I don't understand you"
        return chatty_response, False
    else:
        chatty_response = chatty_response+orig_ans_sent_tokens[idx].strip()
        return chatty_response, True