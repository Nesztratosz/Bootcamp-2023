"""
1 Create a list of the items
2 Create the directories for Stock/Prices
3 loop through the list
    multiple each index with the other dictionary same index
    add together all
"""

menu = ["Tea","Latte","Cappuchino","Espresso","Flat_white"]
price = {"Tea" : 0.80,
      "Latte" : 2.5,
      "Cappuchino" : 2.5,
      "Espresso" : 1.5,
      "Flat_white" : 2
      }

stock = {"Tea" : 25,
         "Latte" : 30,
         "Cappuchino" : 27,
         "Espresso" : 20,
         "Flat_white" : 18
         }

total = 0
for i in price:  #loop through the list and add them together
    value = price[i] * stock[i]
    total = total + value
print(f"The sum total stock of the cafe is  {total} £")


#This part I actually looked it up and just find it nice and neat
total = {i: price * stock[i] for i, price in price.items()}
print(total)
