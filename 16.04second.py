with open('16 april/24_demo.txt') as file:
    sequence = file.read()
    count = 0
    maximum_count = 0
    for element in range(len(sequence) - 1):
        if sequence[element - 1] != sequence[element]:
            count += 1
            if count >= maximum_count:
                maximum_count = count
        else:
            count = 1
    print(maximum_count)
            