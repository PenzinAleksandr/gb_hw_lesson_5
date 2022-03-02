from sys import getsizeof


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

my_gen = ((name, klasses[i]) if i < len(klasses) else (name, None) for i, name in enumerate(tutors))
print(type(my_gen), getsizeof(my_gen))
print(*my_gen)
