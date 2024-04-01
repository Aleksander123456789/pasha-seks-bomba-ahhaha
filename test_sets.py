print("hello world")
total = 0
with open('table.txt') as file:
    lines = file.readlines()
    rows = [list(map(int, row.split())) for row in lines]
    colums = [[row[i] for row in rows] for i in range(6)]
    for row in rows:
        if len(set(row)) != 6:
            continue
        count = 0
        for i, n in enumerate(row):
            
            # 35 33 13 5 98 6
            # i = 0
            # n = 35
            if colums[i].count(n) > 150:
                count += 1

            
        if count >= 5:
            total += 1
print(f'Ответ: {total}')            

