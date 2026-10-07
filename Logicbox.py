while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("\nEnter your choice:")

    if choice == "1":
        rows = int(input("Enter the Number of row :-"))
        print("\nPattern:")
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == "2":
        start = int(input("Enter the starting number:-"))
        end = int(input("Enter the ending number:-"))
        total_sum = sum(range(start, end + 1))      #minore use AI
        print("total sum is:-", total_sum)

    elif choice == "3":
        print("Exit")
        break

    else:
        print("Invalid number...please enter a number 1 , 2 or 3")
