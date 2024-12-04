
numbers: list[int]
"""это ГЛАВНЫЙ СПИСОК МОЕЙ ПРОГРАММЫ"""

with open('17_09april.txt') as file:
    
    numbers = [int(line) for line in file.readlines()]
    count = 0
    max_end_13 = max(number for number in numbers if abs(int(str(number).endswith('13'))))
    
    min_summa = 9999999999999999
    
    for i in range(len(numbers)-2):
        if (99 < abs(numbers[i]) < 1000  and 99 < abs(numbers[i+1]) < 1000 and 100 > len(str(numbers[i+2]).replace('-','')) != 3) or \
           (99 < abs(numbers[i]) < 1000  and 99 < abs(numbers[i+2]) < 1000 and 100 > len(str(numbers[i+1]).replace('-','')) != 3) or \
           (99 < abs(numbers[i+1]) < 1000  and 99 < abs(numbers[i+2]) < 1000 and 100 > len(str(numbers[i]).replace('-','')) != 3):
               sum_triple = numbers[i] + numbers[i+1] + numbers[i+2]
               if sum_triple < max_end_13:
                    count += 1
                    
                    # if sum_triple < min_summa:
                    #     min_summa = sum_triple
                        
                    min_summa = min(sum_triple, min_summa)
                    
            
        else:
            continue
    print(f'Количество троек: {count}')
    print(f'Минимальная сумма: {min_summa}')
    