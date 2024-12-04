#41
def remove_words(s, n):
    words = s.split()
    result = []
    
    for word in words:
        if words.count(word) != n:
            result.append(word)
    
    return ' '.join(result)

input_string = input('Введите строку : ')
n = int(input('Введите число : '))
result = remove_words(input_string, n)
print(result)  
