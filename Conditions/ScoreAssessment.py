score=float(input("please enter your score:"))
if (score<0 and score>100):
    print("enter the correct score")
if (80<score<=100):
    print("you got 'A'")
elif (60<=score<=80):
    print("you got 'B'")
else:
    print("you got 'C'")
