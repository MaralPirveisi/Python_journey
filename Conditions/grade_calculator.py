name=input("Please Enter Your Name:")
score1=float(input("Score1:"))
score2=float(input("Score2:"))
score3=float(input("Score3:"))
average=(score1+score2+score3)/3
print(f'Student {name} Average is {average}')
if average>=17:
    print("WOW..you are a star")
elif 12<=average<17:
    print("GOOD..keep studying")
else:
    print("You need to work harder")
