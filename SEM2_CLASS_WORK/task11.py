# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

# Чи́сла Фибона́ччи (вариант написания — Фибона́чи[2]) — элементы числовой последовательности
# в которой первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел[3]

# 1  2  3  4  5  6  7  8  
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, … (последовательность A000045 в OEIS),


# A = int(input('каким по счету числом Фибоначчи является: '))#5
# fib = 1
# itog=0 #значение числа фибоначчи относительно введенного порядкого номера
# p_minus2=0 #переменная для запоминания пред-предыдущего числа для фибоначчи
# i=0#счётчик
# while  A>itog:   
#     itog=itog+p_minus2
#     p_minus2=fib 
#     fib=itog    
#     i=i+1
# if A==itog:
#     print('Порядковый номер', i)
# else:
#     print('Не является фибоначчи')



# n = int(input())
# n0 = 0
# n1 = 0
# n2 = 1
# i = 2 # Так как 2 первых числа уже известны это 0 и 1
# while n0 < n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
#     if n0 > n:
#         i = 0
# if i != 0:
#     print(i)
# else:
#     print(-1)


# #Вводим число - показываем значение числа фибоначчи.
# A = int(input('Введите число: '))#5
# fib = 1
# itog=0 #значение числа фибоначчи относительно введенного порядкого номера
# p_minus2=0 #переменная для запоминания пред-предыдущего числа для фибоначчи
# i=1#счётчик
# while A>=i:       
#     itog=itog+p_minus2 
#     p_minus2=fib
#     fib=itog      
#     i=i+1         
# print('Число фибоначчи: ', itog)
# #---Конец--- #Вводим число - показываем значение числа фибоначчи.


n = int(input('Введите число: '))#5
i=3
count = 3
fib_1 = 1
fib_2 = 1
fib_i = 0
while fib_i<n:
    fib_i=fib_1+fib_2
    fib_1=fib_2
    fib_2=fib_i
if fib_i!=n:
    print(-1)
else:
    print(count)