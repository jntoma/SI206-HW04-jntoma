def CheckQuestion():
    if question[-1] == "?":
        print(picked_answer)
    else:
        print("I'm sorry, I can only answer questions!")

def Question():
    question = input("What is your question?" )
    return question
