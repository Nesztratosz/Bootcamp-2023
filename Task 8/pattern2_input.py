


num = int(input("please give me number: "))
symbol = "*"
for i in range(num):
        if i < num/2 :
                print(symbol * i)
        else :
                index = (num - i)
                print(symbol * index)