"""
it will go up til 5 since 6 isnt in then it will go down and that will give the pattern
"""

symbol = "*"
for i in range(10):
    if i < 5:
        print(symbol * i)
    else :
        index = (10 - i)
        print(symbol * index)