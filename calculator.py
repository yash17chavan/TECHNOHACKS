def add(x,y):
    return(x+y)
def substract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def division(x,y):
    return(x/y)

num1=eval(input("Enter the First Number: "))
num2=eval(input("Enter the Second Number: "))

print("Select the option")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

while(True):
  choice=int(input("Enter the choice from 1/2/3/4/5 : "))
  if choice in (1,2,3,4,5):
    if choice==1:
      print("Addition of two numbers",num1, "and" ,num2, ":",add(num1,num2))
    elif choice==2:
      print("Substraction of two numbers",num1, "and" ,num2, ":",substract(num1,num2))
    elif choice==3:
      print("Multiplication of two numbers",num1, "and" ,num2, ":",multiply(num1,num2))
    elif choice==4:
      print("Division of two numbers",num1, "and" ,num2, ":",division(num1,num2))
    elif choice==5:
      print("Thankyou")
      exit()
  else:
    print("Invalid Choice try again")
