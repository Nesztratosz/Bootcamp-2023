"""
1 ask the user for a sentence
2 calculate the length of the sentence
3 find the last letter
4 replace the last letter with @
replace every same character to @
5 print the last 3 character backwards
6 look for the first 3 and last two letter and put them together

"""

strmanip = input("Please give me a sentence: ")
#calculation of length
print(len(strmanip))

strmanip_last = strmanip[-1]
print(strmanip_last)

# replace last letter
last =strmanip[:-1] + "@"
print(last)

#replace letter to @
rep = strmanip.replace(strmanip_last, "@")
print(rep)


#backward last 3 letters
strmanip_three = strmanip[-1:-4:-1]
print(strmanip_three)

#Together the first 3 and last 2 letters
three = strmanip[0:3]
print(three)
second = strmanip[-2:]
print(second)
five = three+second
print(five)

