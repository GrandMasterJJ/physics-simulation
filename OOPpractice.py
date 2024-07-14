class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
class Dog:
    def __init__(self, name):
        self.name = name
    def bark():
        print("bark")
    
class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_students = max_student
        self.students = []
    
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("sam", 19, 95)
s2 = Student("ben", 50, 65)
s3 = Student("fred", 10, 60)

d1 = Dog("BB")

course = Course("Math",2)
course.add_students(s1)
course.add_students(s2)
#course.add_students(s3)
#course.add_students(d1)


print(course.students[0].name)
print(course.add_students(s3))
print(course.get_average_grade())
