# Write a program to compute distance between two points taking input from the user 

x1= int(input("enter X1 value "))
y1= int(input("enter y1 value "))
x2= int(input("enter X2 value "))
y2= int(input("enter y2 value "))

result=(((x2-x1)**2 + (y2-y1)**2)**0.5)
print("the distance between two points",(x1,x2),"and",(y1,y2),"=",result)


# Addition of two numbers :- 
num1 = int(input("Enter first number:")) 
num2 = int(input("Enter second number:"))

sum = num1 +num2

print("the sum of two number is:" , sum , type(sum))