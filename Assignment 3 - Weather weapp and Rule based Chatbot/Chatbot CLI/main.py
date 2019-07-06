import utils
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

if __name__== "__main__":
    orig_ques_sent_tokens, orig_ans_sent_tokens = utils.read_corpus()
    ques_sent_tokens, ans_sent_tokens = utils.lemmatize_sentences(orig_ques_sent_tokens, orig_ans_sent_tokens)
    print("\nChatty: Hello there! This is Chatty!\n\tI'm a chatbot that answers questions related to\n\tAbraham Lincoln\n\n\tAsk me anything you'd like.\n\tEnter \"Exit\" when you wish to exit")
    while True:
        query = input()
        if query=="Exit":
            print("\nChatty: Bye!! It was nice talking to you")
            break
        resp = utils.greeting(query)
        if resp != "Normal":
            print("\nChatty:", resp.capitalize())
            continue
        resp,valid = utils.response(query,ques_sent_tokens,orig_ans_sent_tokens)
        print("\nChatty:",resp)
        if not valid:
            print("\nChatty: Can you possibly tell me the answer for this query?\n\tIf yes, please tell the answer!\n\tIf no, just say No and then we can talk further :)")
            ans = input()
            if ans=="No":
                print("\nChatty: No problem :)\n\tLet's continue talking!")
            else:
                orig_ques_sent_tokens.append(query)
                orig_ans_sent_tokens.append(ans+"\n")
                lemmatizer = WordNetLemmatizer()
                qsinit = word_tokenize(query)
                qsfinal = lemmatizer.lemmatize(qsinit[0])
                for word in qsinit[1:]:
                    qsfinal += (" " + lemmatizer.lemmatize(word))
                ansinit = word_tokenize(ans)
                ansfinal = lemmatizer.lemmatize(ansinit[0])
                for word in ansinit[1:]:
                    ansfinal += (" " + lemmatizer.lemmatize(word))
                ques_sent_tokens.append(qsfinal)
                ans_sent_tokens.append(ansfinal+"\n")

                print("\nChatty: Thanks a lot for sharing!")
    utils.write_corpus(orig_ques_sent_tokens,orig_ans_sent_tokens)