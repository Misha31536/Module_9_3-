first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер', 'Компьюfтер', 'Коgпьюfтер']

first_result = (len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1]))

print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(len(min(first, second))) )

print(list(second_result))