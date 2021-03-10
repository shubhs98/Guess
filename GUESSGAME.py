import random as r

num = r.randrange(100)
Guess = 5

while Guess >=0:
    your_guess = int(input("enter the number"))

    def check(x):
        if your_guess==x:
            print("you win")
        elif your_guess > x:
            print("Please keep trying lower number")
        else:
            print("Please keep trying higher number")

    if Guess >1:
            check(num)
    elif Guess == 1:
            print("this is your last turn")
    else:
            print("you lost")
            Guess = Guess - 1

