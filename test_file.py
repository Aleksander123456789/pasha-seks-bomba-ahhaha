result = 0
with open('text_file.txt') as file:
    lines = file.readlines()    
    for line in lines:
        a = list(map(int, line.split()))
        if len(set(a)) != len(a) - 1:
            continue
        
        for n in a:
            if a.count(n) == 2:
                repeated_number = n
                break

        avg_non_repeated_numbers = (sum(a) - 2*repeated_number) / 4
        if avg_non_repeated_numbers > repeated_number:
            print(a)
            result += 1
        
        
print(result)