users=["maral","sara","ali","reza","maral","ali"]
li=[]
for user in users:
    if user not in li:
        li.append(user)
    if user in li:
        pass
print(li)
