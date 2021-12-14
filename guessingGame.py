#(9)Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
try:
    n=(random.randint(1,9))
    # print(n)
    a=int(input("guess integer between 1 to 9."))
    if a>n:
        print("too high.")
    elif a<n:
        print("too low.")
    else:
        print("exact.")
except:
    print("Please enter valid input.")