import random
class Student:
    def __init__(self, name, grade):
        self.name = name 
        self.grade = random.choice(grade)

    def __str__(self):
        return self.name

grade = ["A", "B", "C", "D", "E", "F"]


student_1 = Student("Alice", grade)
student_2 = Student("Jack", grade)
student_3 = Student("John", grade)
student_4 = Student("Mary", grade)
student_5 = Student("Max", grade)

print(f"{student_1} has {student_1.grade} rank")
print(f"{student_2} has {student_2.grade} rank")
print(f"{student_3} has {student_3.grade} rank")
print(f"{student_4} has {student_4.grade} rank")
print(f"{student_5} has {student_5.grade} rank")