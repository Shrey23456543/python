class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
        
r1=rect(l=int(input("Enter a number:")),b=int(input("Enter second number:")))
ans=r1.area()
print(ans)
