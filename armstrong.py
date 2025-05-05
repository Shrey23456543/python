num = int(input("Enter a number: "))
sum = 0
temp = num
n = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if sum == num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

