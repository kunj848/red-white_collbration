import datetime

name = input("Enter your name:- ")
age = int(input("Enter your age:-"))
height = float(input("Enter your height in s.mitter:- "))
favourite_number = int(input("Enter your favourite number:- "))

current_year =2026
birth_year = current_year - age

height_as_int = int(height)


print("\n      PERSONAL DATA & ANALYSIS")
print("     --------------------------")

print("\nName:", name)
print("Data Type:", type(name))
print("Memory ID:", id(name))

print("\nAge:", age)
print("Data Type:", type(age))
print("Memory ID:", id(age))

print("\nHeight:", height, "meters")
print("Data Type:", type(height))
print("Memory ID:", id(height))

print("\nFavourite Number:", favourite_number)
print("Data Type:", type(favourite_number))
print("Memory ID:", id(favourite_number))

print("\n      CALCULATION & CONVERSION ")
print("     --------------------------")

print("\nCurrent Year:", current_year)
print("Birth Year:", birth_year)
print("Calculation:", current_year, "-", age, "=", birth_year)

print("\nHeight Conversion:")
print("Float Value:", height)
print("Integer Value:", height_as_int)
print("Converted Data Type:", type(height_as_int))
print("New Memory ID:", id(height_as_int))

print("\n---------PROCESS IS COMPLETE---------")

