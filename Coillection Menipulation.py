students = []

while True:
    print("Select the option:")
    print("1. ddd Student")
    print("2. Display All Students")
    print("3. exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("\nEnter student detail:")
        student_id = input("Student id: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth (DD-MM-YYYY): ")
        subjects = input("Subjects (comma-separated): ")
        
       
        student = { "id": student_id,
                    "name": name,
                    "age": age,
                    "grade": grade,
                    "dob": dob,
                    "subjects": subjects  }

            
        students.append(student)
        print("\nStudent add to successfuly\n")
        
    elif choice == "2":
        print("\nDisplay the all the student details")
        if not students:
            print("No students found.\n")
        else:
            for s in students:
                print(f"\nStudent ID: {s['id']}")
                print(f"\nName: {s['name']}")
                print(f"\nAge: {s['age']}")
                print(f"\nGrade: {s['grade']}")
                print(f"\nDate of Birth: {s['dob']}")
                print(f"\nSubjects: {s['subjects']}")
                print("-" * 20)
                
            print()
            
    elif choice == "3":
        print("Exit the programe")
        break
    else:
        print("Invalid choice. please enter the choice beetween the 1 to 3\n")
