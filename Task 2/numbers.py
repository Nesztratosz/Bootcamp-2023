"""
1 ask the user to enter 3 number
2 add all the numbers together
3 num1 minus num2
4 num3 multiply by num1
5 sum off all num divided by num3
"""

numone = input("Please give me my first number: ")
numtwo = input("please give me a second number: ")
numthree = input("please give me my last number: ")
print("your numbers are " + numone + " " + numtwo + " " + numthree)

#convert them to integer for calculating
num1 = int(numone)
num2 = int(numtwo)
num3 = int(numthree)

#sum them up
together = num1 + num2 + num3
print(together)

#first minus the second number
minus = num1 - num2
print(minus)

#multiple 1st and 3rd number
multi = num1 * num3
print(multi)

#summ all together and divide by num 3
div = together / num3
print(div)