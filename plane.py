#2.2.6
str1 = input("Введите первую строку чисел через пробел: ")
str2 = input("Введите вторую строку чисел через пробел: ")
list1 = list(map(int, str1.split()))
list2 = list(map(int, str2.split()))
common_list = list1 + list2

n = len(common_list)
for i in range(n-1):
    for j in range(n-1):
        if common_list[j] > common_list[j+1]:
            common_list[j], common_list[j+1] = common_list[j+1], common_list[j]

print(common_list)
