# PQSTPQSTPP
with open('02april.txt') as file:
    sequence  = file.read()
    count = 1
    maximum_count = 0
    for element in range(1, len(sequence)):
        if sequence[element] == 'P' and sequence[element-1] == 'P':
            if count >= maximum_count:
                maximum_count = count
            count = 1
        else:
            count += 1
    
    print(maximum_count, count)
    print(len(sequence))