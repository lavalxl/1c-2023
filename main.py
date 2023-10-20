import Levenshtein
import os

# Считываем вводные данные
print("Введите первую директорию:")
directory_1 = str(input())
print("Введите вторую директорию:")
directory_2 = str(input())
print("Введите минимальный процент сходства:")
min_percent = int(input())

# Получение списка файлов в директориях
files_in_d1 = os.listdir(directory_1)
files_in_d2 = os.listdir(directory_2)
set_1 = set(files_in_d1)
set_2 = set(files_in_d2)

# Сравнение файлов и вывод
for file_name_1 in files_in_d1:
    for file_name_2 in files_in_d2:
        with open(f'{directory_1}/{file_name_1}', 'r') as f1:
            s1 = f1.read()
        with open(f'{directory_2}/{file_name_2}', 'r') as f2:
            s2 = f2.read()
        lev_size = Levenshtein.distance(s2, s1)
        s1_size = len(s1)
        s2_size = len(s2)

        if s1_size > s2_size:
            dif_percent = int(float(s1_size - lev_size) / s1_size * 100)
        else:
            dif_percent = int(float(s2_size - lev_size) / s2_size * 100)

        if dif_percent >= min_percent:
            set_1.discard(file_name_1)
            set_2.discard(file_name_2)
            print(file_name_1, 'похож на', file_name_2, 'на', f'{dif_percent}%', sep=' ', end='\n')

# Выводим файлы которые есть лишь в одной директории
if set_1:
    print('Файлы:', set_1, 'есть в директории 1, но их нет в директории 2')
if set_2:
    print('Файлы:', set_2, 'есть в директории 2, но их нет в директории 1')