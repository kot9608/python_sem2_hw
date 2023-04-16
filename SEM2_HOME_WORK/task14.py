# Задача 14: 
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

# Пример
# Ввод: 17 -> Вывод: 1, 2, 4, 8, 16

max=int(input('Введи число: '))

i=0#счётчик
if max==0 or max==1:
  print('NULL')
else:
   while 2**i<max:
    print(2**i)
    i=i+1


# right_side = int(input('right side: '))
# degree = 0
# nums = []
# while 2**degree <= right_side:
# nums.append(2**degree)
# degree += 1
# print(nums)

# right_side = int(input('right side: '))
# degree = 0
# nums = {}
# while 2**degree <= right_side:
# nums[degree] = 2**degree
# degree += 1
# print(nums)