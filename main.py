from random import randint, sample
import sort
import search

# Генерация случайных чисел для работы
num = sample(range(0,100), 20)
val = randint(0,100)

# Распечатка сгенерированного листа с числами
print(num)

# Функция сортировки по алгоритму Bubble sort и распечка отсортированного листа с числами
num = sort.bubble_sort(num)
print(num)

# Распечатка сгенерированного числа для поиска
print(f'Поиск элемента {val}')

# Функция для поиска числа по схеме двоичного поиска
search.binary_search(val, num)