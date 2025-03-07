students = ['Mary', 'Rop','Joseph']
#accessing elements in list
# print(students[1])
#append method
students.append('Mercy')
# print(students)
#insert
students.insert(1,'John')
# print(students)
teachers = ['ben', 'bett']
students.extend(teachers)
# print(students)
#concatenation
africode_community = students + teachers
#combined list
# print(africode_community)
#*******remove elements
students.remove('ben')
# print(students)
students.pop()
# print(students)
# del students

students.clear()