current_year = 2026
age = int(input("Enter your age: "))

current_year=int(input("Enter your current year:-"))

birth_year = current_year - age

if birth_year < 2000:
    print("Born before 2000")
elif birth_year > 2000:
    print("Born after 2000")
else:
    print("Born in 2000")
