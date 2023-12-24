a = []
b = int(input())
if b > 0:
    a.append(b)
else:
    print("Введите положительное число!")


while len(a) != 2 and b != 0:
    b = int(input())
    if b > 0:
           a.append(b)
    elif b < 0:
        print("Введите положительное число!")
    if len(a) == 2:
        print(f'{a[0]} + {a[1]} = {sum(a)}')
        print(f'{a[0]} - {a[1]} = {a[0] - a[1]}')
        print(f'{a[0]} * {a[1]} = {a[0]*a[1]}')
        print(f'{a[0]} / {a[1]} = {a[0]/a[1]}')
        print('')
        a = []

