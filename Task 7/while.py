"""
1 ask for a number
while the number is >=0
    sum+ input
    count +1
    ask again
    if input is -1
    break
then  average = sum / count
    print average

"""

print("Give the programe a number it will add together")
print(" and if you give -1 to it stops and give you the average of it")
sum1 = 0
pieces = 0
given_number = int(input("PLease give me a number: "))
while given_number > -1:
        sum1 += given_number
        pieces += 1
        given_number = int(input("PLease give me a number: "))
        if given_number == -1:
            print(sum1)       #left these to line in for double checking
            print(pieces)
            average = sum1 / pieces
            print(f"Average of your numbers {average}")
            break

