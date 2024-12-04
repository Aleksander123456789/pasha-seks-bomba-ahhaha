#17672
f = open('09_17672.csv')
count = 0
for s in f:
    a = list(map(int, s.split(';')))
    a.sort()
    if max(a) + min(a) < (a[0] + a[1] + a[2] + a[3]) - (max(a) + min(a)):
        count += 1
print(count)

    