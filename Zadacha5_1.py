# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def power_numbers(a, b):
    if b == 0:
        return 1
    if b < 0:    
        return 1 / power_numbers(a, -b)
    if b % 2 == 0:
        return power_numbers(a, b // 2) * power_numbers(a, b // 2)   
    else:
        return power_numbers(a, b - 1) * a
print(power_numbers(2, 4))