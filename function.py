from first import *
import csv 

# def student_system(student):
students = [{}]
while True  :
  print("\nStudent Management System")
  print("1. Add Student")
  print("2. Update Student Marks")
  print("3. Calculate Average Marks")
  print("4. Find Highest Marks in a Subject")
  print("5. Display All Students")
  print("6. Exit")

  choice = int(input("Enter your choice: "))


  if choice == 1:
      add_student(students)
  elif choice == 2:
      roll_no = int(input("Enter Roll Number: "))
      update_marks(students, roll_no)
  elif choice == 3:
      roll_no = int(input("Enter Roll Number: "))
      print(f"Average Marks: {calculate_average(students, roll_no)}")
  if choice == 4:
      subject = input("Enter Subject (Math/Science/English): ")
      highest_marks(students, subject)
  elif choice == 5:
      display_students(students)
  elif choice == 6:
      break
  else:
      print("Invalid choice! Please try again.")



with open('vani.csv', 'r', newline='') as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)