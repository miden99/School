import json


# ____
def re(data, file_name):
    file = open(file_name, 'w', encoding='UTF-8')
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()


# ___
def get_index(data, fullname):
    for teacher in data:
        if teacher['surname']+' '+teacher['name'] == fullname:
            return data.index(teacher)


Students = json.load(open('Students_id.json', 'r'))
Teachers = json.load(open('Teachers_id.json', 'r'))

surname = 'Иванов'
list_id = []


# 2
def student_surname(data, file_name):
    for el in file_name:
        if data == el['surname']:
            list_id.append(el['id'])
    for el in file_name:
        for elID in list_id:
            if elID == el['id']:
                print(el['surname']+' '+el['name']+' '+el['middle_name'])
# student_surname(surname, Students)

classroom = '7 В'
teaid=[]


# 3
def teacher_id(data, file_name):
    for el in file_name:
        if data in el['class']:
            teaid.append(el['id'])
    print(teaid)
teacher_id(classroom, Teachers)


