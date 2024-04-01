result = 0
with open('second_trxt.txt') as file:
    print("hello world")
    lines = file.readlines()

    for line in lines:
        a = list(map(int, line.split()))

        if len(set(a)) != 4:
            continue
        
        for n in a:
            if a.count(n) == 4:
                repeated_word = n
                break
        else:
            continue
        total = (sum(a) - 4*repeated_word)/3
        if total < repeated_word:
            print(a, repeated_word, total)
            result += 1
        
    print(result)


# [1, 1, 1, 1, 9, 10, 11]
# set(...) = {1, 9, 10, 11}

# [1, 1, 1, 3, 3, 10, 11]
# set(...) = {1, 3, 10, 11}