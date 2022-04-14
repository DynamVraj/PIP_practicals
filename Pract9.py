'''
    20CS059
    VRAJ PATEL
'''
class student:
    Name = 'Vraj'
    id = 0

def details(self, id, Name):
    self.Name = Name
    self.id = id

class exam(student):
    list = []

def marks(self, list):
    self.list = list
    return list

class final(exam):
    m = 0

def result(self, m):
    total = 0
    for item in m:
        total += item
    return total

sobj = final()
name = input("Enter the name of the student : ")
id = input("Enter the Roll Number of the student : ")

sobj.details(id, name)
print(f"Enter the marks of {name} in 6 subject : \n")
marks = []
for i in range(0, 6):
    marks.append(int(input()))

m = sobj.marks(marks)
total = sobj.result(m)
print(f"Total of {name} marks are : {total}")
