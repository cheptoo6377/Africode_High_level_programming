# for i in range (1,10,2):#start from 1, end at 10, increment by 2
#     print(i)
students = ["John", "Juma", "James","jackie"]
# for student in students:
#     print(student)
# students = set(students)
# for student in students:
#   print(student)
# adding another variable
# count = 1
# for student in students:
#     print(count, student)
#     count += 1
# using len and range
# for  index in range(len(students)):
#     print(index, students[index])
# set_students = set(students)
# for  index in range(len(set_students)):
#   print(index, set_students[index])# error because set does not support indexing
# using enumerate
# list
# for i , student in enumerate(students):
#     print(i+1, student)
#pass
# for student in students:
#     pass
for student in students:
    if student == "Juma":
        continue
    print(student)
else:
    print("the list ends here")