count = 0
while count < 3:
    username = input("Enter username: ")
    password = int(input("Enter password: "))

    if username == 'Neel':
        if password == neel2007:  
            print(" valid username and password")
            break
        else:
            print("Invalid password")
    else:
        print("Invalid username")
        
