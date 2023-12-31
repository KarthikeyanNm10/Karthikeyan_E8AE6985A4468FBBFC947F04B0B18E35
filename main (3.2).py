class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students
# Creating a list of student objects
students = [
    Student("Unknown 1", "S001", 3.9),
    Student("Unknown 2", "S002", 3.7),
    Student("Unknown 3", "S003", 3.5),
    Student("Unknown 4", "S004", 3.8),
]
sorted_students = sort_students(students)

for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")