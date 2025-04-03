class Students:
    def enrol (self):
        pass
    def graduate (self):
        pass
class Graduates(Students):
    def enrol(self):
        return "enrolling in the program"
    def graduate(self):
        return "graduated"
vague_student = Graduates()
print(vague_student.graduate())