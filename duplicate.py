S=input("Enter a string:")
res=""
for char in S:
    if char not in res:
        res+=char
print(res)
