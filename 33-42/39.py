from string import ascii_letters
a = input('Введите строку: ')
k = 0
l = list()

if a[-1] not in ascii_letters:
    l.append(1)

for x in a:
    if x not in ascii_letters:
        k += 1
    else:
        l.append(k)
        k = 0

print(max(l))