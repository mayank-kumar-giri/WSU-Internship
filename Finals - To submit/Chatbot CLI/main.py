import utils

if __name__== "__main__":
    ques_sent_tokens, ans_sent_tokens = utils.read_corpus()
    print("\nChatty: Hello there! This is Chatty!\n\t\tI'm a chatbot that answers questions related to\n\t\tAbraham Lincoln\n\n\t\tAsk me anything you'd like.\n\t\tEnter \"Exit\" when you wish to exit")
    while True:
        query = input()
        if query=="Exit":
            print("\nChatty: Bye!! It was nice talking to you")
            break
        resp = utils.greeting(query)
        if resp != "Normal":
            print("\nChatty:", resp.capitalize())
            continue
        resp,valid = utils.response(query,ques_sent_tokens,ans_sent_tokens)
        print("\nChatty:",resp.capitalize())
        if not valid:
            print("\nChatty: Can you possibly tell me the answer for this query?\n\t\tIf yes, please tell the answer!\n\t\tIf no, just say No and then we can talk further :)")
            ans = input()
            if ans=="No":
                print("\nChatty: No problem :)\n\t\tLet's continue talking!")
            else:
                ques_sent_tokens.append(query)
                ans_sent_tokens.append(ans+"\n")
                print("\nChatty: Thanks a lot for sharing!")
    utils.write_corpus(ques_sent_tokens,ans_sent_tokens)