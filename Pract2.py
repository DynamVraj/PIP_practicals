'''
    20CS059
    VRAJ PATEL
'''



'''Dictionary'''
def Merge(Student1,Teacher) :
    return (Teacher.update(Student1))
Student1 = {
    'Name': 'VRAJ PATEL',
    'Id': '20CS059',
    'Age': '18'
}
print(Student1)
#a
print('Name' in Student1)
print('Id' in Student1)
print('Age' in Student1)

Teacher = {
    'fn': 'Ayushi Chaudari',
    'Address': 'Changa'
}
#b
print(Merge(Student1, Teacher))
print(Teacher)
#c
d1 ={
     'a': 100,
     'b': 250
}
print(sum(d1.values()))
#d
d1['c'] = 123
print(d1)
#e
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3) : dic4.update(d)
print(dic4)

'''Tuple'''
#a
difDatatype = ('Hello', 10, 15.456)
#print(difDatatype)

#b
numbers = (1, 2, 3, 4, 5)
print(numbers)

#c
numbers = numbers + (6,)
print(numbers)

#d
def  convertToString(tuple) :
    #intializing an empty string
    str = ''
    for item in tuple:
        str = str + item
    return str


tuple = ('a','b','c','d','e')
str = convertToString(tuple)
print(str)

#e
print(len(tuple))

'''Set'''
#a
set1 = {'hello', 'pyhton'}
print(set1)
set1.add('program')
print(set1)
set1.clear()
print(set1)

#b
phone = {'samsung' , 'iphone' , 'realme'}
print(phone)
phone.remove('iphone')
print(phone)

#c
fruits = {'Apple','Banana','Tomato'}
#print(fruits)
vegetables = {'Potato','Tomato'}
#print(vegetables)
print(fruits.union(vegetables))
print(fruits.intersection(vegetables))

#d
set = { 10 ,63 , 7483 , 128}
print(max(set))
print(min(set))

#e
##for list:
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))

#for tuple
def countX(tup, x):
    count = 0
    for ele in tup:
        if (ele == x):
            count = count + 1
    return count

tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
enq = 4
enq1 = 10
enq2 = 8
print(countX(tup, enq))
print(countX(tup, enq1))
print(countX(tup, enq2))