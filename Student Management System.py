class Student:
    def __init__(self,student_id,name,age,marks):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.marks=marks
        
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        student = Student(student_id, name, age, marks)
        self.students.append(student)
        print("Student added successfully!\n")

   
    def view_students(self):
        if len(self.students) == 0:
            print("No student records found.\n")
        else:
            print("\nStudent Records")
            print("-" * 50)
            for s in self.students:
                print("ID:", s.student_id)
                print("Name:", s.name)
                print("Age:", s.age)
                print("Marks:", s.marks)
                print("-" * 50)


    def search_student(self):
        sid = input("Enter Student ID to search: ")
        for s in self.students:
            if s.student_id == sid:
                print("\nStudent Found")
                print("ID:", s.student_id)
                print("Name:", s.name)
                print("Age:", s.age)
                print("Marks:", s.marks)
                return
        print("Student not found.\n")

  
    def update_marks(self):
        sid = input("Enter Student ID to update marks: ")
        for s in self.students:
            if s.student_id == sid:
                s.marks = float(input("Enter new marks: "))
                print("Marks updated successfully!\n")
                return
        print("Student not found.\n")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")
        for s in self.students:
            if s.student_id == sid:
                self.students.remove(s)
                print("Student record deleted successfully!\n")
                return
        print("Student not found.\n")


    def highest_marks_student(self):
        if len(self.students) == 0:
            print("No student records available.\n")
            return

        highest = self.students[0]
        for s in self.students:
            if s.marks > highest.marks:
                highest = s

        print("\nStudent with Highest Marks")
        print("ID:", highest.student_id)
        print("Name:", highest.name)
        print("Age:", highest.age)
        print("Marks:", highest.marks)
        print()


sms = StudentManagementSystem()

while True:
    print("===== Student Management System =====")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Marks")
    print("5. Delete Student Record")
    print("6. Display Student with Highest Marks")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        sms.add_student()
    elif choice == "2":
        sms.view_students()
    elif choice == "3":
        sms.search_student()
    elif choice == "4":
        sms.update_marks()
    elif choice == "5":
        sms.delete_student()
    elif choice == "6":
        sms.highest_marks_student()
    elif choice == "7":
        print("Exiting Student Management System...")
        break
    else:
        print("Invalid choice! Please try again.\n")