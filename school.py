import json

Stu=json.load(open('Students.json'))
Teach=json.load(open('Teachers.json'))


list=[]
#1.Задание
for el in Stu:
    list.append(el['name'])
print('1.Ученики',list)
list=[]


#2.Задание

for el in Teach:
    list.append(el['name'])
print('2.Учителя',list)
list=[]


#3.Задание

# clas=input()
clas='6 А'
for el in Stu:
    if clas==el['class']:
        print('3.',clas,'-',el['name'],el['middle_name'])


# 4.Задание

for el in Stu:
    list.append(el['school'])
for el in Teach:
    list.append(el['school'])
print('4.Школы',set(list))
list=[]

# for el in Stu and Teach:
#     print(el['school'])


# 5.Задание

for st in Stu:
    surname=st['surname']
    i=0
    for el in Stu:
        if el['surname'] == surname:
            i+=1
            if i==2:
                print('5.',st['name'],' ',st['surname'])


# 2.1 Задание

class_list = []
teach_name = 'Владимир Вышкин'
for teacher in Teach:
  if teach_name == '%s %s' % (teacher['name'], teacher['surname']):
    class_list = teacher['class']

for el in class_list:
  for student in Stu:
    if student['class'] == el:
        print('2.1', student['surname'], student['name'], student['middle_name'])

# 2.2 Задание
student_full_name = 'Иван Иванов'
for student in Stu:
  if student['name'] + ' ' + student['surname'] == student_full_name:
    for teacher in Teach:
        if student['school'] == teacher['school'] and student['class'] in teacher['class']:
            print('2.2',teacher['name'] + ' ' + teacher['middle_name'] + ' ' + teacher['surname'])
  break