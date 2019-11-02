# Import modules
import sys
import random

ans = True

while ans:
    question = input(
        "Ask the Magic 8 Ball a question: (press enter to quit)")

    answers = random.randint(1, 21)

    if question == "":
        sys.exit()

# Positive Answers

    elif answers == 1:
        print("It is certain")

    elif answers == 2:
        print("It is decidely so")

    elif answers == 3:
        print("Without a doubt")

    elif answers == 4:
        print("Yes - definitely")

    elif answers == 5:
        print("Signs point to yes")

    elif answers == 6:
        print("As I seet it, yes")

    elif answers == 7:
        print("As I see it, yes")

    elif answers == 8:
        print("Outlook good")

    elif answers == 9:
        print("You may rely on it")

    elif answers == 10:
        print("Yes")

# Non-committal answers

    elif answers == 11:
        print("Concentrate and ask again")

    elif answers == 12:
        print("Reply hazy, try again")

    elif answers == 13:
        print("Most likely")

    elif answers == 14:
        print("Better ask again later")

    elif answers == 15:
        print("Cannot predict now")

# Negative answers

    elif answers == 16:
        print("Don't count on it")

    elif answers == 17:
        print("My reply is no")

    elif answers == 18:
        print("My sources say no")

    elif answers == 19:
        print("Outlook not so good")

    elif answers == 20:
        print("Very doubtful")

    elif answers == 21:
        print("The anwser is 42")
