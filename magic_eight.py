import random
import sys

def Question():
    question = input("What is your question?" )
    return question

def random_answer():
    answers = ["It is certain", "As I see it, yes", "Reply hazy try again",
                "Don't count on it", "It is decidedly so", "Most likely",
                "Ask again later", "My reply is no", "Without a doubt",
                "Outlook good", "Better not tell you now", "My sources say no",
                "Yes definitely", "Yes","Cannot predict now", "Outlook not so good",
                "You may rely on it", "Signs point to yes", "Concentrate and ask again",
                "Very doubtful"]

    picked_answer = random.choice(answers)
    return picked_answer


question = ""
if question == "quit":
    sys.exit()

while question != "quit":
    question = Question()
    if question[-1] != "?" and question != "quit":
        print("I’m sorry, I can only answer questions.")
    elif question == "quit":
        sys.exit()
    else:
        print(random_answer())
