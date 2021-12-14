#(8) Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
z=1
p1=0
p2=0
while(z==1):

    n1=input("choose Player 1 option(rock/paper/scissors):-")
    n2=input("choose Plater 2 option(rock/paper/scissors):-")

    if n1=="rock" and n2=="paper":
        print("Hurray! player 2 wins.")
        p2+=1
    elif n1=="rock" and n2=="scissors":
        print("Hurray! player 1 wins.")
        p1+=1

    elif n1=="paper" and n2=="scissors":
        print("Hurray! player 2 wins.")
        p2+=1
    elif n1=="paper" and n2=="rock":
        print("Hurray! player 1 wins.")
        p1+=1

    elif n1=="scissors" and n2=="rock":
        print("Hurray! player 2 wins.")
        p2+=1
    elif n1=="scissors" and n2=="paper":
        print("Hurray! player 1 wins.")
        p1+=1
    
    z=(int(input("for play again enter 1 and stop any other number:-")))

print("FINAL RESULT OF THE GAME IS, PLAYER 1 HAS {} POINT AND PLAYER 2 HAS {} POINT.".format(p1,p2))



