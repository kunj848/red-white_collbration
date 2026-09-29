dress = "Formal"
age = 20
new_dress=input("what are you wearing:-")
age=int(input("enter your age:-"))


if(age>=18):
    if(dress == new_dress):
        print("welcome and Allowed the party")

    else:
        print("not cloths wear")
else:
    print("age is not validated")
