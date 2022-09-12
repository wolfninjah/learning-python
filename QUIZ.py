import random

score = 0


def question_store():
    a = []
    a.append(["What's the biggest animal in the world?", "The blue whale"])
    a.append(["What is the smallest country in the world?", "Vatican City"])
    a.append(["What is the hottest continent on Earth?", "Africa"])
    a.append(["What is the largest country in the world?", "Russia"])
    a.append(
        ["In football, which team has won the Champions League (formerly the European Cup) the most?", "Real Madrid"])
    a.append(["Who won the FIFA Women's World Cup in 2019", "USA"])
    a.append(["Which year was the Premier League founded?", "1992"])
    a.append([
                 "Real Madrid won the first five European Cups - but which club was the second to win Europe's elite competition?",
                 "Benifica"])
    a.append(["What colour is found on 75% of the world’s flags?", "Red"])
    a.append(["Who discovered Penicillin?", "Alexander Fleming"])
    a.append(["How many cards are there in a playing deck(cards)?", "52"])
    a.append(["The name of the polygon that has 15 sides?", "Pentadecagon"])
    a.append(["What is the other name of the perimeter of a Circle?", "The Circumference"])
    a.append(["Which is the only even prime number?", "2"])
    a.append(["How many seconds are there in an hour?", "3600"])
    a.append(["What is the full form of BODMAS?", "Bracket Of Division Multiplication Addition Subtraction"])
    a.append(["What is the cross between a donkey and a zebra known as?", "Zeedonk"])
    a.append(["Which sea creature has three hearts? ", "Octopus"])
    a.append(["Which European country eats the most chocolate per capita?", "Switzerland"])
    return a


def game_time():
    global score
    question = question_store()
    random.shuffle(question)
    for q in question:
        print("Question: " + q[0])
        print("enter your answer")
        t = input()
        if t.upper() == q[1].upper():
            print("Correct!")
            score = score + 1
        elif t.upper() == "EXIT":
            exit()
        else:
            print("Wrong answer!!")
            print("Correct answer was :" + q[1])


def home():
    print("--------------------------------")
    print("------ WELCOME TO GK QUIZ ------")
    print("-==============================-")
    print("----Press 1 to enter to quiz----")
    print("-==============================-")
    print("--------Press 2 to exit --------")
    print("-==============================-")
    print("-======== Press 1 or 2=========-")
    print("-==Type exit to exit mid game==-")
    p = input()
    if p == "1":
        game_time()
    elif p == "2":
        exit()
    else:
        print(" Wrong input")
        exit()


def bablu():
    global score
    if score <= 10:
        print("Fuck you man , you need some improvements")
    elif score <= 14 and score > 10:
        print("Good job , but shit you are still bad ")
    elif score > 14:
        print("bruhhh !! you got it ..")
    elif score == 19:
        print("Ok !! You were not meant to google the answers !! Fuck you ")


home()
print("Your final score was : " + str(score))
