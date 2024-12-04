#42
def common_words(sentence1, sentence2):

    words1 = sentence1.lower().split()
    words2 = sentence2.lower().split()
    
    common = []
    for word in words1:
        if word in words2 and word not in common:
            common.append(word)
    
    return common


sentence1 = input('Введите строку : ')
sentence2 = input('Введите строку : ')

result = common_words(sentence1, sentence2)
print(result)
