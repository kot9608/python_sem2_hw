# 9. По данному целому неотрицательному n
# вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

num = int(input('Введите число факториал: '))
i = 1 #вспомогательная переменная
factorial_num = 1 #минимальное значение переменной
while num>i:
    #print('Зашли в цикл')
    factorial_num = factorial_num * (num)
    num=num-1
    #print(num, factorial_num)
else: print('Факториал =', factorial_num)