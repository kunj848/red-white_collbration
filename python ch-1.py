# Lesson 1 - Variables

print("\n========== LESSON 1: VARIABLES ==========")

name = "sufiyan"
age = 29
course = "Data Analysis"

print(name)
print(age)
print(course)


# Lesson 2 - Data Types

print("\n========== LESSON 2: DATA TYPES ==========")

print(type(name))
print(type(age))
print(type(course))


# Lesson 3 - Input

print("\n========== LESSON 3: INPUT ==========")

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Name:", user_name)
print("Age:", user_age)


# Lesson 4 - Operators

print("\n========== LESSON 4: OPERATORS ==========")

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# Lesson 5 - If Else

print("\n========== LESSON 5: IF ELSE ==========")

marks = 75

if marks >= 90:
    print("A grade")
elif marks >= 60:
    print("B grade")
else:
    print("C grade")


# Lesson 6 - for Loop

print("\n========== LESSON 6: FOR LOOP ==========")

for a in range(1,6):
    print(a)

for b in range(1,11):
    print(b)

# Lesson 7 - While Loop

print("\n========== LESSON 7: WHILE LOOP ==========")

count = 1

while count <=5:
    print(count)
    count=count+1

# Lesson 8 - List

print("\n========== LESSON 8: List ==========")

names = ["sufiyan", "Ali", "Ahmed", "Rahul"]

print(names)

names.append("Raj")

print(names)
           
