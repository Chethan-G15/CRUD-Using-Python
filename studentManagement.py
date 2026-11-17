from student import Student
class StudentManagement:
    def __init__(self):
        self.students=[]

    # for creating the Student
    def createStudent(self,id,name,age):
        student = Student(id,name,age)
        self.students.append(student)
        print("Student Details Added Sucessfully")

    # display the Student
    def displayStudent(self):
        for i in self.students:
            print("Student Id ",i.id)
            print("Student name ",i.name)
            print("Student age ", i.age)
            print("--------------------")

    # update student details
    def updateStudent(self,id,name,age):
        for student in self.students:
            if student.id == id:
                student.name = name
                student.age =age
                print("Student updated Sucessully")
                return
            print("Student Not Found")

    #deleteStudent Record 
    def deleteStudent(self,id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                print("Student Deleted Sucessfully")
                return
            print("Sudent Not Found")