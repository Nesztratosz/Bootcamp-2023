"""
1 make a variable with the sentence
2 change the ! to " "
3 print out with upper letters
4 reverse the sentence
"""

sentence = "The!quick!fox!jumps!over!the!lazy!dog"
print(sentence)
sentence_replace = sentence.replace("!" , " ")
print(sentence_replace)
sentence_upper = sentence.upper()
print(sentence_upper)
sentence_reverse = sentence_replace[: :-1]
print(sentence_reverse)

