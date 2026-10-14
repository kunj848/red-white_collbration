lst = []

value = input("please enter name, marks and age separated by spaces")
value  = value.split()
dict1 = {"name", value[0], "mark": value[1], "age": value[2]}
lst.append(dict1)
