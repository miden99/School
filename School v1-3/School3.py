import json


# ____
def re(data, file_name):
    file = open(file_name, 'w', encoding='UTF-8')
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()


# ___
def get_index(data, full_name):
    for teachers in data:
        if teachers['surname'] + ' ' + teachers['name'] == full_name:
            return data.index(teachers)


student = {
    "name": "Максим",
    "middle_name": "Григорьевич",
    "surname": "Степанов",
    "school": "67 школа",
    "class": "6 А",
    "birth_day": "10.05.1999"
}
teacher = {
    "name": "Алексей",
    "middle_name": "Владиславович",
    "surname": "Черный",
    "school": "67 школа",
    "class": [
        "6 А",
        "6 Г",
        "7 Г"
    ],
    "birth_day": "03.08.1976"
}


with open('Students_id.json', 'r') as Student1:
    with open('Teachers_id.json', 'r') as Teacher1:
        studentL = json.load(Student1)
        teacherL = json.load(Teacher1)

# 3 номер
        new_class = '5 Г'
        teacherL.append(teacherL[get_index(teacherL, 'Вышкин Владимир')]['class'].append(new_class))

# 1 номер
#         l = 1
#         lst = ['id']
#         for el in student:
#             l += 1
#         lst.append(l)
#         studentL.update([lst])
#         studentL.append(student)
#         re(student, 'Students_id.json')
#
#         l = 1
#         lst = ['id']
# # 2 номер
#         for el1 in teacherL:
#             l += 1
#         lst.append(l)
#         teacher.update([lst])
#         teacherL.append(teacher)
#         re(teacherL, 'Teachers_id.json')

# 4 номер
#         studentL.pop(get_index(studentL, 'Кузин Артем'))
#         re(studentL, 'Students_id.json')
#
# #  5 номер
#         class_room = '6 А'
#         for el in studentL:
#             if el['class'] == class_room:
#                 studentL.pop(get_index(studentL, el['surname']+' '+el['name']))
#         re(studentL, 'Students_id.json')
#
# 6 номер
#         teacherL.pop(get_index(teacherL, 'Черный Александр'))
#         re(teacherL, 'Teachers_id.json')
#
# 7 номер
#         school = '67 шк'
#         for el in teacherL:
#             if el['school'] == school:
#                 teacherL.pop(get_index(teacherL, el['surname']+' '+el['name']))
#         re(teacherL, 'Teachers_id.json')
#
# 8 номер
#         new_class = '6 Г'
#         fullname = 'Вышкин Владимир'
#         for el in teacherL:
#             if el['surname']+' '+el['name'] == fullname:
#                 for class_room in el['class']:
#                     if class_room == new_class:
#                         index = el['class'].index(class_room)
#                         el['class'].pop(index)
#         re(teacherL, 'Teachers_id.json')
#         teacherL[get_index(teacherL, 'Вышкин Владимир')]['class'].remove(new_class)
#         re(teacherL, 'Teachers_id.json')
#         pass
#     pass
