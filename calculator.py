#creating class Calculator
class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mult(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return "Cannot divide by zero."
        else:
            return a/b
    def mod(self,a,b):  #remainder
        return a%b
#object of class Calculator
calc=Calculator()
#Getting user input
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

while True:
    print("1.Add")
    print("2.Sub")
    print("3.Mult")
    print("4.Div")
    print("5.Mod")
    
    ch=input("Enter operation:").lower()
    if ch=="exit":
        print("Calculator closed !")
        break
    
    if ch=="add":
        print("Result:",calc.add(a,b))
    elif ch=="sub":
        print("Result:",calc.sub(a,b))
    elif ch=="mult":
        print("Result:",calc.mult(a,b))
    elif ch=="div":
        print("Result:",calc.div(a,b))
    elif ch=="mod":
        print("Result:",calc.mod(a,b))
    else:
        print("Invalid Choice")
        continue  #ask again
    