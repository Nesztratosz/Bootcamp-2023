"""
1 need to ask the user to give the time they got in the triathlon in minutes
  swimming
  running
  cycling
2 calculate and display the times
3 if time under 100 min provincial colours
4 if time between 101 to 105 half provincial colours
5 if time between 106 to 110 provincial scroll
6 if over 111+ then no award
"""

swimming = input("Please give me your swimming time in minutes: ")
cycle = input("please give me your cycling time in minutes: ")
running = input("please give me your running time in minutes: ")
#convert the times into integers
s = int(swimming)
c = int(cycle)
r =int(running)
t = s + c + r
print(f"You done your triathlon in {t} minutes")
if t < 100:
    print("Congratulations you get a Provincial colours Award")
elif t >= 101 and t <= 105:
    print("Congratulations you get a Provincial Half colours Award")
elif t >= 106 and t <= 110:
    print("Congratulations you get a Provincial Scroll Award")
else :
    print("Well done for participating")
