"""
1 take details
    name
    age
    house number
    street name
2 give it out as a full sentence
"""

name = input("Please give me your name: ").capitalize()
age = input("PLease give me your age: ")
house_number = input("Please give me your house number: ")
street = input("Please give me your street name: ").capitalize()
sentence ="This is " + name + " they are " + age + " live in " + house_number + " " + street + " Street!"
# I tried f string but somehow it dont working please give me a hint what im doing wrong Thanks
"""sentence =f"This is "{name}" they are "{age}" live in "{house_number}" "{street}" Street!"""
print(sentence)