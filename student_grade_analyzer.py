def add_student(Students): # we are passing to the function a list
    name = input("Enter your name: ")
    grade = float(input("Enter your grade (0-100): "))

    Student = {"name": name, "grade": grade}
    Students.append(Student)
    print(f"The student {name} is added to the list with the grade {grade}")


def display_students (Students): #students is a list
    if not Students:
        print("No student added to the list yet")
        return
    print("\n ------ ALL THE STUDENTS ------")
    for student in Students:
        print (f"{student['name']}:{student['grade']}")
    print()

def main():
    students = []
    while True:
        print(" ------ STUDENT GRADE ANALYZER ------")
        print("1. ADD STUDENTS")
        print("2. DISPLAY STUDENTS")
        print("3. Exit")

        while True:  #this is like a do while loop, since it does not exist in python
            choice = input ("Enter choice (1-3): ") #no need to conver to an int since i only need the value i wont be doing any arithmatic operations on them
            if choice in ["1", "2", "3"]:
                break
            else:
                print("Invalid input, please enter a valid number")


        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        else:
            print("GOODBYE!!")
            break

if __name__ == "__main__":   # this controlls when the main runs, it tell it to run only if it is the main funtion and not if it is impoted, since if it is imported it will have another name (the name of the function)
    main()


        

