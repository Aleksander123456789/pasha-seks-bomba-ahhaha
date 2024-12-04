n = int(input('Колво студентов: '))
m = int(input('Колво экзаменов: '))

info = list()

k = 0

for student in range(n):
     name = input('Имя студента: ')
     info.append(list())
     info[student].append(name)
     for ozenka in range(m):
        oz = int(input(f'Оценка {ozenka+1}: '))
        info[student].append(oz)

for student in info:
    if student.count(5) == m:
        k += 1

print(k)