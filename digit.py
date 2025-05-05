a=int(input("Enter a number"))
original=a
rev=0
while a>0:
    digit=a%10
    rev=rev*10+digit
    a=a//10
print(rev)
if original==rev:
    print("Yes it is palindrome")
else:
    print(" Not")
