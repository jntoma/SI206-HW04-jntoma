def Question():
    question = input("What is your question? ")
    return question

while Question() != "quit":
    if question[-1] != "?":
        print("I'm sorry, I can only answer questions!")
    else:
        print(picked_answer)
