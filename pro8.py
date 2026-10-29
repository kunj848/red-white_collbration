payment = int(input("Enter payment :"))
total_payment = 0
while(True):
    if(payment == 0):
       break

    else:
        total_payment = total_payment+payment
        payment = int(input("Enter payment :"))

print(total_payment)
