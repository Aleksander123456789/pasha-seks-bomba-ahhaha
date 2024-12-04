#35
def unique_characters(s):
    return ''.join([char for char in s if s.count(char) == 1])

input_string = input('Введите строку из символов: ')
result = unique_characters(input_string)
print(result)