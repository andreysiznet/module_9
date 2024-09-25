first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(word)  for word in first_strings if len(word) >= 5]
second_result = [(word,word_1) for word in first_strings for word_1 in second_strings if len(word) == len(word_1)]
sum_ = first_strings + second_strings
third_result = {word:len(word) for word in sum_ if len(word) % 2 ==0 }




print(first_result)
print(second_result)
print(third_result)
