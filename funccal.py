class Calculator():
     def __init__(self,num1,num2):
         self.num1=num1
         self.num2=num2
    
     def add(self):
        return self.num1+self.num2
     def sub(self):
        return self.num1-self.num2
     def mul(self):
        return self.num1*self.num2
     def div(self):
        return self.num1/self.num2

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

cl=Calculator(num1,num2)
ans1 = cl.add()
ans2 = cl.sub()
ans3 = cl.mul()
ans4 = cl.div()
print("Addition of num1 and num2 is:",ans1)
print("Substraction of num1 and num2 is:",ans2)
print("Multiplication of num1 and num2 is:",ans3)
print("Division of num1 and num2 is:",ans4)
     
