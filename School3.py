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

#______

Students = json.load(open('Reserv.json', 'r'))
Teachers = json.load(open('TeachReserv.json', 'r'))

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


# 3 номер
# new_class = '5 Г'
# Teachers.append(Teachers[get_index(Teachers, 'Вышкин Владимир')]['class'].append(new_class))

# 1 номер
# Students.append(student)
# re(Students,'Reserv.json')

# 2 номер
# Teachers.append(teacher)
# re(Teachers,'TeachReserv.json')

# 4 номер
# Students.pop(get_index(Students, 'Кузин Артем'))
# re(Students, 'Reserv.json')

#  5 номер
clas = '6 А'
for el in Students:
    if el['class'] == clas:
        Students.pop(get_index(Students, el['surname']+' '+el['name']))
re(Students, 'Reserv.json')