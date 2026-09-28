first_name = input("Enter First Name: ")

middle_name = input("Enter Middle Name (optional): ")

last_name = input("Enter Last Name: ")



if middle_name == "":

    full_name = first_name + " " + last_name

else:

    full_name = first_name + " " + middle_name + " " + last_name



print("Full Name:", full_name) 