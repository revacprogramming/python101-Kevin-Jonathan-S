# Variables, Expressions & Statements

def Compute(hrs,rate,pay):
   pay=float(hrs)*float(rate)
   return pay

hrs = input("enter the no of hours: ")
rate = input("enter the rate: ")

Compute(int(hrs),int(rate), int(pay))
print("The total pay is: ", pay)