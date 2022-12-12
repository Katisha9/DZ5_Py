# Задача 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def zipp(string):
    count = 1
    result = ''
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            result = result + str(count) + string[i]
            count = 1
    if count > 1 or (string[len(string) - 2] != string[-1]):
        result = result + str(count) + string[-1]
    return result


def unzipp(string):
    repeat_num = ''
    result = ''
    for i in range(len(string)):
        if not string[i].isalpha():
            repeat_num += string[i]
        else:
            result = result + string[i] * int(repeat_num)
            repeat_num = ''
    return result


with open('file1.txt', 'r') as data:
    s = data.readline()

print(f'Текст после сжатия: {zipp(s)}')
with open('file2.txt', 'w') as data:
    data.write(zipp(s))

print(f'Текст после восстановления: {unzipp(zipp(s))}')
