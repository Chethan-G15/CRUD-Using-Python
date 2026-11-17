from studentManagement import StudentManagement
obj = StudentManagement()

obj.createStudent(1, "Rahul", 22)
obj.createStudent(2, "Priya", 23)

print("\nAll Students:")
obj.displayStudent()

print("\nUpdating Student:")
obj.updateStudent(1, "Rahul", 25)

print("\nDeleting Student:")
obj.deleteStudent(2)

print("\nFinal Student Details:")
obj.displayStudent()