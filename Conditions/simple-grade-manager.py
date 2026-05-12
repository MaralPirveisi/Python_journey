li=[10,14,20,19,8,15]
summation=0
for el in li:
    summation+=el
    if el>=17:
        print(f" score {el} :you can get scholarship")
    elif el>=10:
        print(f" score {el} :passed")
    else:
        print(f" score {el} :failed")
average=summation/len(li)
print(f"class average is {average}")
