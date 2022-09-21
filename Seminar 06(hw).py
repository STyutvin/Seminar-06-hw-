# Задача №1. Сгенерируйте случайный список из чисел.
# Увеличьте значение каждого элемента на 10 и запишите в новый список.

# def rand_list(n):
#     from random import randint
#     some_list=[]
#     for i in range(n):
#         some_list.append(randint(1,10))
#     return some_list

# x=int(input('Введите количество элемнтов массива: '))
# s1=rand_list(x)
# print(s1)
# s2=list(map(lambda y: y+10, s1))
# print(s2)
#------------------------------------------------------

# Задача №2. Задан список возрастов некоторых людей. Выберите всех взрослых, возраст которых от 18 и больше, и выведите отдельным списком.
# ages = [5, 12, 17, 18, 24, 32]
# adults=list(filter(lambda x: x>=18, ages))
# print(adults)
#------------------------------------------------------

# Задача №3. Задайте два числовых списка. На их основе создайте общий список, убрав одинаковые элементы.

# def rand_list(n): 
#     from random import randint
#     some_list=[]
#     for i in range(n):
#         some_list.append(randint(1,10))
#     return some_list
# k=int(input('Количество элементов для списка s1: '))
# m=int(input('Количество элементов для списка s2: '))
# s1=rand_list(k)
# s2=rand_list(m)
# print(s1)
# print(s2)

# def filter_duplicate(string_to_check):
#     if string_to_check in ll:
#         return False
#     else:
#         return True

# ll = s2
# s3 = list(filter(filter_duplicate, s1))
# ll = s1
# s3 += list(filter(filter_duplicate, s2))
# print(list(tuple(filter(lambda num: s3.count(num) == 1, s3)))) # это на случай, если в одном из списков сгенерируются несколько одинаковых элементов
#------------------------------------------------------

# Задача №4. Задан текстовый файл, в котором числа записаны в строку через пробел. Посчитайте сумму чисел в файле.
data = open('f01.txt')
num_list=(data.readlines())
new_str=(''.join(num_list))
print(new_str)
new_list=new_str.split()
print('Сумма чисел в файле: ', sum(map(int, new_str.split())))