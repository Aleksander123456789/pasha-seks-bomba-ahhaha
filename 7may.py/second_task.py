with open('24_ege2022_day2.txt') as file:
    line = file.read()
    line = line.replace('PNO','*').replace('NPO', '*')
    for i in range(1000):
        if i * '*' in line:
            print("FOUND:", i)
        else:
            break
    # print(i-1)
