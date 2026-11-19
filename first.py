def highest_marks(students, subject):
  max = 0
  for highest in students :
    if highest[subject] > max :
      max = highest[subject]
    print(max)
    print(highest["name"])


def add_student(students):
  print()
  print("~~"*20)
  print()
  name = input("Enter student name                   --> ".title())
  print()
  roll = int(input("Enter student roll number          -->  "))
  print()
  computer = int(input("Enter  student Computer  marks -->  "))
  print()
  science = int(input("Enter  student Science marks    -->  "))
  print()
  math = int(input("Enter  student Math marks          -->  "))
  print()
  hindi = int(input("Enter  student Hindi marks        -->  "))
  print()
  english = int(input("Enter  student English marks    -->  "))
  if computer > 100 or science > 100 or math > 100 or hindi > 100 or english > 100 :
    print("Cheater  :(")
    print()
    sorry = input("Say sorry for this mistake \n : ")
    if sorry == "sorry":
      print("~~"*20)
      print()
      name = input("Enter student name                   --> ".title())
      print()
      roll = int(input("Enter student roll number          -->  "))
      print()
      computer = int(input("Enter  student Computer  marks -->  "))
      print()
      science = int(input("Enter  student Science marks    -->  "))
      print()
      math = int(input("Enter  student Math marks          -->  "))
      print()
      hindi = int(input("Enter  student Hindi marks        -->  "))
      print()
      english = int(input("Enter  student English marks    -->  "))
    else :
      n = 0
      while n <= 2000 :
        n =  n + 1
        print("cheater"*n,"Cheater :(")

  student = {
      "name":name.title(),
      "roll_no" : roll,
      "computer": computer,
      "science": science,
      "math": math,
      "hindi": hindi,
      "english": english
      }
  print("**"*20)
  students.append(student)


def display_students(students):
  for student in students:
      values = list(student.values())
      print()
      print("Name     -->", values[0])
      print("Roll_no  -->", values[1])
      print("Computer -->", values[2])
      print("Science  -->", values[3])
      print("Math     -->", values[4])
      print("Hindi    -->", values[5])
      print("English  -->", values[6])
      print()
      print("~`~"*20)
      print()
      print()



def update_marks(students, roll_no):
  for student in students:
    if student["roll_no"] == roll_no:
      print("Edit student Data ''Please!! Handle with care'' ")
      student['hindi']= int(input("Enter student hindi marks         --> "))
      student["english"] = int(input("Enter student english marks    --> "))
      student["math"] = int(input("Enter student math marks          --> "))
      student["computer"] = int(input("Enter student computer marks  --> "))
      student["science"] = int(input("Enter student science marks    --> "))
      print()
      print("Marks Updated Successfully")
      break
  else :
    print("Please again conform your roll no ")



