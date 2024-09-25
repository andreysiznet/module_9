first = ['Strings', 'Student', 'Computers']

second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(word) - len(word_1) for word, word_1 in zip(first, second) if len(word) != len(word_1))

second_result = (len(first[word]) == len(second[word]) for word in range(len(first)))

print(list(first_result))
print(list(second_result))
