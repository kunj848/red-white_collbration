day = int(input("Enter a Number Beetween 1 to 7 :-"))

match day:

    case 1:
        print( "Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Satuerday")

    case 7:
        print("Sunday")

    case _Other_Number:
        print("\nPlease Enter valid Number! Enter Number Beetween 1 to 7 ")
