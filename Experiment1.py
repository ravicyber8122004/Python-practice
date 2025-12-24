print("Numeric data tupes:- ")

a = 5
print("Integer:" , a , type(a))

b =7.5
print("Float:" , b , type(b))

c = 3+4j
print("Complex number:" , c , type(c))


print("Boolean data type:-")

p = True
q = False
print("Boolean p:" , p , type(p))
print("Boolean q:" , q , type(q))

print("String data type:")
s = "Hello,world"
print("String s: " , s , type(s))

print("List data type ")

num = [1,2,3,4,4,"five"]
print("List num:" , num , type(num))

print("Tuple data type ")

coordinates = (20,20)
print("tuple" , coordinates , type(coordinates))

print("Set data type ")

fruits = {"apple" , "apple" , "cherry"}
print("Set "  , fruits , type(fruits))

print("Dictionary data type ")

person = {
    "name" :"Ravi",
    "course":"B.tech",
    "age": 21
}

print("Dictionary:", person , type(person))




# WAP to add two number input should be taken from user 

num1 = int(input("Enter first number:")) 
num2 = float(input("Enter second number:"))

sum = num1 +num2

print("the sum of two number is:" , sum , type(sum))


num1 = int(input("Enter first number:")) 
num2 = int(input("Enter second number:"))

sum = num1 +num2

print("the sum of two number is:" , sum , type(sum))



num1 = float(input("Enter first number:")) 
num2 = float(input("Enter second number:"))

sum = num1 +num2

print("the sum of two number is:" , sum , type(sum))


num1 = eval(input("Enter first number:")) 
num2 = float(input("Enter second number:"))

sum = num1 +num2

print("the sum of two number is:" , sum , type(sum))

# Write a program to check that a given number is even or odd

num = int(input("Enter the num"))
if num % 2 == 0:
        print("Given num is Even",num)
else:
        print("Given num is odd",num)

# find largest among two number 

num1 = int(input("Enter a num1 "))
num2 = int(input("Enter the num2 "))

if num1>num2:
        print(num1,"is greater")

elif num2>num1:
        print(num2,"is greater")
else:
        print("both num is equal")


# check that the given number is prime or not

num = 7
for i in range(2,num):
        if num > 1:
                if num % i == 0:
                        print("Not a prime")
                        break
                else:
                        print("prime num")
                        break
        else:
                print("Not a prime")
                
              


# Calculate CI and take the value from the user.

P = int(input("Enter the principle value"))
R = float(input("Enter the rate of interest "))
T = int(input("Enter the timeline in year"))


CI = P*(1+R/100)**T
print("Simple interest is " ,CI-P)