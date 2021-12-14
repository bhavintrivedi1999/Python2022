#(1)Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
from datetime import date
todays_date = date.today()
cr=todays_date.year
name=input("Enter your name:-")
age=int(input("Enter your age:-"))
x=100-age + cr
print("hey on the {} year you will become 100 years old.".format(x))