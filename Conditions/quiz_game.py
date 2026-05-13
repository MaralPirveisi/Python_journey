score = 0
answer1 = input("What is the capital of Iran? ")
if answer1.lower() == "tehran":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer2 = input("What is 5 + 3? ")
if answer2 == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer3 = input("Which programming language are we learning? ")
if answer3.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print(f"Your final score is {score}/3")
