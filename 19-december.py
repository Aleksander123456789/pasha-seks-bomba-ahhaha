numbers = list(map(float, input('ввод 20 чисел: ').split()))
previous = numbers[0]
for i in range(len(numbers)):
    if previous > numbers[i]:
        print(numbers[i])
        pass





