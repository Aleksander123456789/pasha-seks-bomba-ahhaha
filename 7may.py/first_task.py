with open('107_24.txt') as file:
    line = file.read()
    count = 0
    counts = []
    line = line.replace('AB','*')\
                .replace('CB', '*')
    
    # for i in line:
    #     if i == '*' or i =='*':
    #         count += 1
    #     else:
    #         count = 0
    #     counts.append(count)
    # print(max(counts))
    
    for i in range(100):
        if i * '*' in line:
            print(i-1)
        else:
            break
    # print(i)
            
    