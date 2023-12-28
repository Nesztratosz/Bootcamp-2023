"""
1 we going to ask for a sentence
2 we going to go througth the letter 1 by one and every second one we change for upper case
3 we do the same but instead the even number letters the odd ones will change to upper
4 we going to slice the string to list
5 and every second element in the list will be upper case
"""

sentence = input("Please give me a sentence: ")
upper_sentence = ""
lower_sentence = ""
new_sentence = ""
split_sentence = sentence.split()

#this part is turning the sentence every second one upper case
for i in range(len(sentence)):
    if i % 2 == 1:
       upper_sentence += sentence[i].upper()
    else:
       upper_sentence += sentence[i].lower()
print(upper_sentence)

#this part is turning the sentence every second one lower case
for i in range(len(sentence)):
    if i % 2 == 1:
       lower_sentence += sentence[i].lower()
    else:
       lower_sentence += sentence[i].upper()

print(lower_sentence)

#this part is splitting and upper case every second word
for i in range(len(split_sentence)):
   if  i % 2 == 1:
        new_sentence += split_sentence[i].upper() + " "
   else:
        new_sentence += split_sentence[i].lower() + " "
print(new_sentence)
