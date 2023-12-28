"""
1 Ask the user it age
2 if over 100 then print Sorry you are dead
3 if age is over then 65 print enjoy retirement
4 if age is over 40 print you are over the hill
5 if age is 21 print congrats on your 21
6 if age is under 13 print you are qualify for kiddie discount
7 else just write age is but a number
"""


age = int(input("Please enter your age: "))
if age > 100:
    print("Sorry you are dead!")
elif age > 65:
    print("Enjoy your retirement!")
elif age >40:
    print("You are over the hill")
elif age == 21:
    print("Congratulation on your 21st")
elif age <13:
    print("You are qualify for kiddie discount")
else:
    print("Age is but a number")