"""
Challange 1
1 ask 3 sides of the triangle
2 calc the area of the triangle
print out the area of the triangle

"""
import math

side1 = input("please give a length of the first side: ")
side2 = input("please give a length of the second side: ")
side3 = input("please give a length of the third side:")
sentence =f"These are the measurements you provided  {side1}  {side2} {side3}"
print(sentence)
#convert to integer
s1 = float(side1)
s2 = float(side2)
s3 = float(side3)
s = ((s1+s2+s3)/2)
print(s)
#t1 is so you dont get math error since it would start with the square root but still need o calc the number out it breaks
t1=(s*(s-s1)*(s-s2)*(s-s3))
print(t1)
t = math.sqrt(t1)
print((t))

#"(s*(s-s1)*(s-s2)*(s-s3))"