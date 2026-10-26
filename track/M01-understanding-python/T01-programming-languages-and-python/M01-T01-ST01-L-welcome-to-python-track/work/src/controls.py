number=int(input("Enter a number: "))
if number > 0:
    print("Number is positive")
elif number == 0:
    print("Number is zero")
else:
    print("Number is negative")

age=int(input("Enter your age: "))
if age>=18:
    print("Eligible to donate blood")
else:
    print("Not eligible to donate blood")


temperature=int(input("Enter the temperature: "))
if temperature>30:
    print("Hot weather")
elif temperature>=10:
    print("Warm weather")
else:
    print("Cold weather")

attendance = int(input("Enter the attendance percentage: "))
if attendance >= 75:
    print("Eligible for class A")
elif attendance >= 55:
    print(" Eligible for class B")
else:
    print("Not eligible for class C")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

age = int(input("Enter your age: "))
if age>=18:
    print("Eligible for to apply for a driving licenese")
else:
    print("Not eligible for a driving license")
    

year = int(input("Enter the year: "))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

num1=float(input("enter the number 1: "))
num2=float(input("enter the number 2: "))

if num1>=num2:
    print(" first number is greater",num1)
else:
    print("second number is greater",num2)    

marks=int(input("Enter the marks: "))
if marks>=90-100:
    print("Grade: A")
elif marks>=80-89:
    print("Grade: B")
elif marks>=70-79:
    print("Grade: C")
elif marks>=60-69:
    print("Grade: D")
else:
    print("Grade: F")    

units = int(input("Enter the number of units: "))
if units > 500:
    print("Category: High power consumer")
elif units >=301:
    print("Category: Medium power consumer")
elif units >=201:
    print("Category: Low power consumer")
else:
    print("Category: Very Low power consumer")

marks=float(input("enter the marks"))
family_income = float(input("enter the family income"))
if marks>=90 and family_income>=800000:
    print("Eligible for scholarship")
elif marks>=80 and family_income>=500000:
    print("Eligible for scholarship")
    
 username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password":
    print("Login successful")
else:
    print("Invalid credentials")    
    