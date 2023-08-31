"""ITF 08 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name :Ahed Hazem
Delivery Date :31\8\2023
"""
# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)
import uuid

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark

# Example usage
course_name = input("Enter the course name: ")
course_mark = float(input("Enter the course mark: "))
course = Course(course_name, course_mark)

print("Course ID:", course.course_id)
print("Course Name:", course.course_name)
print("Course Mark:", course.course_mark)
 # class Student:
 # # TODO 3 define static variable indicates total student count
class Student:
    total_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_students += 1


print("Total students:", Student.total_students)  # Output: 2
# TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    # def __init__(self):
    #     pass
import uuid


class Student:
    total_students = 1


    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []

        Student.total_students += 1


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark

class Student:
    def __init__(self, student_number, name, scores):
        self.student_number = student_number
        self.name = name
        self.scores = scores
        self.courses = []

    def enroll_new_course(self, course_name, course_mark):
        course = {"name": course_name, "mark": course_mark}
        self.courses.append(course)

    def get_student_details(self):
        return {
            "student_number": self.student_number,
            "name": self.name,
            "scores": self.scores,
            "courses": self.courses
        }

    def get_student_courses(self):
        return self.courses


# Sample student data for demonstration
students = [
    Student("123", "Alice", [85, 90, 78]),
    Student("456", "Bob", [92, 88, 75]),
    Student("789", "Charlie", [80, 85, 90])
]

while True:
    selection = int(input("Enter your selection: "))

    if selection == 6:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                student.enroll_new_course(course_name, course_mark)
                print("Course added successfully.")
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid selection. Please try again.")
#######################################################
class Student:
    def __init__(self, student_number, name, scores):
        self.student_number = student_number
        self.name = name
        self.scores = scores
        self.courses = []

    def enroll_new_course(self, course_name, course_mark):
        course = {"name": course_name, "mark": course_mark}
        self.courses.append(course)

    def get_student_details(self):
        return {
            "student_number": self.student_number,
            "name": self.name,
            "scores": self.scores,
            "courses": self.courses
        }

    def get_student_courses(self):
        return self.courses

    def print_student_courses_with_marks(self):
        if not self.courses:
            print("No courses enrolled yet.")
        else:
            print("Courses with Marks:")
            for course in self.courses:
                print(f"Course: {course['name']}, Mark: {course['mark']}")

    def get_student_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)


# Sample student data for demonstration
students = [
    Student("123", "Alice", [85, 90, 78]),
    Student("456", "Bob", [92, 88, 75]),
    Student("789", "Charlie", [80, 85, 90])
]

while True:
    selection = int(input("Enter your selection: "))

    if selection == 6:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                student.enroll_new_course(course_name, course_mark)
                print("Course added successfully.")
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 7:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student.student_number == student_number:
                student.print_student_courses_with_marks()
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 8:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student.student_number == student_number:
                average = student.get_student_average()
                print("Student Average:", average)
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 9:
        print("Exiting the program.")
        break
    else:
        print("Invalid selection. Please try again.")
#################################################################3
import uuid

#
# class Student:
#
#
# # ... (same as before)
#
# class Course:
#
#
# # ... (same as before)

students = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit: "))

        if selection == 1:
            student_number = input("Enter Student Number: ")

            # Check if the student number already exists
            if any(student.student_number == student_number for student in students):
                print("Student number already exists.")
            else:
                student_name = input("Enter Student Name: ")

                while True:
                    try:
                        student_age = int(input("Enter Student Age: "))
                        break
                    except ValueError:
                        print("Invalid Value. Please enter a valid age.")

                # Create the new student instance and add it to the students list
                new_student = Student(student_name, student_age, student_number)
                students.append(new_student)

                print("Student added successfully!")

        # ... (other menu options)

        elif selection == 6:
            print("Exiting...")
            break
        else:
            print("Invalid selection. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")
###########################################################3
class Student:
    def __init__(self, student_number, name, scores):
        self.student_number = student_number
        self.name = name
        self.scores = scores
        self.courses = []

    def enroll_new_course(self, course_name, course_mark):
        course = {"name": course_name, "mark": course_mark}
        self.courses.append(course)

    def get_student_details(self):
        return {
            "student_number": self.student_number,
            "name": self.name,
            "scores": self.scores,
            "courses": self.courses
        }

    def get_student_courses(self):
        return self.courses

    def print_student_courses_with_marks(self):
        if not self.courses:
            print("No courses enrolled yet.")
        else:
            print("Courses with Marks:")
            for course in self.courses:
                print(f"Course: {course['name']}, Mark: {course['mark']}")

    def get_student_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)


# Sample student data for demonstration
students = [
    Student("123", "Alice", [85, 90, 78]),
    Student("456", "Bob", [92, 88, 75]),
    Student("789", "Charlie", [80, 85, 90])
]

while True:
    selection = int(input("Enter your selection: "))

    if selection == 6:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                student.enroll_new_course(course_name, course_mark)
                print("Course added successfully.")
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 7:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student.student_number == student_number:
                student.print_student_courses_with_marks()
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 8:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student.student_number == student_number:
                average = student.get_student_average()
                print("Student Average:", average)
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 9:
        print("Exiting the program.")
        break
    else:
        print("Invalid selection. Please try again.")
#########################################################
students = []

class Student:
    def __init__(self, student_number, name, scores):
        self.student_number = student_number
        self.name = name
        self.scores = scores
        self.courses = []

    # ... other methods ...

while True:
    selection = int(input("Enter your selection: "))

    if selection == 6:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                student.enroll_new_course(course_name, course_mark)
                print("Course added successfully.")
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 7:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student.student_number == student_number:
                student.print_student_courses_with_marks()
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 8:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student.student_number == student_number:
                average = student.get_student_average()
                print("Student Average:", average)
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 9:
        print("Exiting the program.")
        break
    else:
        print("Invalid selection. Please try again.")
###########################################################
students = []

class Student:
# ... class methods ...

 while True:
    try:
        selection = int(input("Enter your selection:\n"
                              "1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to Student with Mark\n"
                              "6.Exit\n"))

        if selection == 1:
            # Add new student code
            pass
        elif selection == 2:
            # Delete student code
            pass
        elif selection == 3:
            # Display student code
            pass
        elif selection == 4:
            # Get student average code
            pass
        elif selection == 5:
            # Add course to student code
            pass
        elif selection == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid selection. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number as your selection.")
##########################################################################
class Student:
    def __init__(self, student_number, name, age):
        self.student_number = student_number
        self.name = name
        self.age = age
        self.scores = []
        self.courses = []

    # ... other methods ...


students = []

while True:
    try:
        selection = int(input("Enter your selection:\n"
                              "1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to Student with Mark\n"
                              "6.Exit\n"))

        if selection == 1:
            student_number = input("Enter Student Number: ")
            student_name = input("Enter Student Name: ")

            # Check if student number already exists
            exists = any(student.student_number == student_number for student in students)
            if exists:
                print("Student with this number already exists.")
            else:
                while True:
                    try:
                        student_age = int(input("Enter Student Age: "))
                        break
                    except ValueError:
                        print("Invalid Value. Please enter a valid age.")

                students.append(Student(student_number, student_name, student_age))
                print("Student added successfully.")

        elif selection == 2:
            # Delete student code
            pass
        elif selection == 3:
            # Display student code
            pass
        elif selection == 4:
            # Get student average code
            pass
        elif selection == 5:
            # Add course to student code
            pass
        elif selection == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid selection. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number as your selection.")
###################################################################3



####################################################
import uuid


# class Student:
#
#
# # ... (same as before)

# class Course:
#
#
# # ... (same as before)

students = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit: "))

        if selection == 1:
            student_number = input("Enter Student Number: ")

            # Check if the student number already exists
            if any(student.student_number == student_number for student in students):
                print("Student number already exists.")
            else:
                student_name = input("Enter Student Name: ")

                while True:
                    try:
                        student_age = int(input("Enter Student Age: "))
                        break
                    except ValueError:
                        print("Invalid Value. Please enter a valid age.")

                # Create the new student instance and add it to the students list
                new_student = Student(student_name, student_age, student_number)
                students.append(new_student)

                print("Student Added Successfully!")

        elif selection == 2:
            student_number = input("Enter Student Number to delete: ")
            found = False

            for student in students:
                if student.student_number == student_number:
                    students.remove(student)
                    found = True
                    print("Student Deleted Successfully!")
                    break

            if not found:
                print("Student not found with the provided number.")

        # ... (other menu options)

        elif selection == 6:
            print("Exiting...")
            break
        else:
            print("Invalid selection. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Sample student data for demonstration
students = [
    {"student_number": "123", "name": "Alice", "scores": [85, 90, 78]},
    {"student_number": "456", "name": "Bob", "scores": [92, 88, 75]},
    {"student_number": "789", "name": "Charlie", "scores": [80, 85, 90]}
]

selection = 5
student_number = input("Enter Student Number: ")

found = False

if selection == 5:
    for student in students:
        if student["student_number"] == student_number:
            scores = student["scores"]
            average = sum(scores) / len(scores)
            print("Student Average:", average)
            found = True
            break

if not found:
    print("Student Not Exist")

# Sample student data for demonstration
students = [
    {"student_number": "123", "name": "Alice", "scores": [85, 90, 78], "courses": []},
    {"student_number": "456", "name": "Bob", "scores": [92, 88, 75], "courses": []},
    {"student_number": "789", "name": "Charlie", "scores": [80, 85, 90], "courses": []}
]

selection = 6  # Assuming this is the menu option for adding a course
student_number = input("Enter Student Number: ")

found = False

if selection == 6:
    for student in students:
        if student["student_number"] == student_number:
            course_name = input("Enter Course Name: ")
            course_mark = float(input("Enter Course Mark: "))
            course = {"name": course_name, "mark": course_mark}
            student["courses"].append(course)
            print("Course added successfully.")
            found = True
            break

if not found:
    print("Student Not Exist")

# Sample student data for demonstration
students = [
    {"student_number": "123", "name": "Alice", "scores": [85, 90, 78], "courses": []},
    {"student_number": "456", "name": "Bob", "scores": [92, 88, 75], "courses": []},
    {"student_number": "789", "name": "Charlie", "scores": [80, 85, 90], "courses": []}
]

def exit_program():
    print("Exiting the program.")
    exit()

while True:
    selection = int(input("Enter your selection: "))

    if selection == 6:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students:
            if student["student_number"] == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                course = {"name": course_name, "mark": course_mark}
                student["courses"].append(course)
                print("Course added successfully.")
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 7:
        exit_program()
else:
print("Invalid selection. Please try again.")


  class Course:
 # ... (same as before)

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = []

    # ... (other methods, like add_course, if needed)


##################################################
# class Course:
#     # ... (same as before)
#
# class Student:
#     # ... (same as before)
#
# # Create a list of student objects (you can populate this list with actual students)
# students = []
#
# # ... (previous code)
#
# elif selection == 3:
#     student_number = input("Enter Student Name or Number: ")
#
#     found_student = None
#     for student in students:
#         if student.name == student_number or student.number == student_number:
#             found_student = student
#             break
#
#     if found_student:
#         students.remove(found_student)
#         print(f"{found_student.name} has been deleted.")
#     else:
#         print("Student Not Exist")

##########################################################
# class Course:
# # ... (same as before)
#
# class Student:
# # ... (same as before)
#
# # Create a list of student objects (you can populate this list with actual students)
# students = []
#
# # ... (previous code)
#
# elif selection == 4:
#     student_number = input("Enter Student Name or Number: ")
#
#     found_student = None
#     for student in students:
#         if student.name == student_number or student.number == student_number:
#             found_student = student
#             break
#
#     if found_student:
#         print(f"Student Name: {found_student.name}")
#         print("Courses:")
#         if len(found_student.courses) == 0:
#             print("No courses registered for this student.")
#         else:
#             for course in found_student.courses:
#                 print(f"Course: {course.name}, Mark: {course.mark}")
#     else:
#         print("Student Not Exist")
#
#################################################################
# # class Course:
# # # ... (same as before)
# #
# # class Student:
# # # ... (same as before)
#
# # Create a list of student objects (you can populate this list with actual students)
# students = []
#
# # ... (previous code)
#
# elif selection == 5:
#     student_number = input("Enter Student Name or Number: ")
#
#     found_student = None
#     for student in students:
#         if student.name == student_number or student.number == student_number:
#             found_student = student
#             break
#
#     if found_student:
#         if len(found_student.courses) == 0:
#             print(f"{found_student.name} has no courses.")
#         else:
#             total_mark = sum(course.mark for course in found_student.courses)
#             average = total_mark / len(found_student.courses)
#             print(f"{found_student.name}'s Average Mark: {average:.2f}")
#     else:
#         print("Student Not Exist")

########################################################
class Course:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

# Assuming you have a student object called 'target_student'
student_name = input("Enter student name: ")
target_student = Student(student_name)

while True:
    course_name = input("Enter course name (or 'exit' to finish): ")
    if course_name.lower() == 'exit':
        break

    course_mark = float(input("Enter course mark: "))
    course = Course(course_name, course_mark)
    target_student.add_course(course)

print(f"{target_student.name}'s Courses:")
for course in target_student.courses:
    print(f"Course: {course.name}, Mark: {course.mark}")

##############################################
import sys

def exit_program():
    print("Exiting the program")
    sys.exit()

exit_program()
