import numpy as np

def printArg(name, arg):
    print(f"{name:10}  dec: {arg:8}, bin: {arg:<15b}")

def cyclic_code_encode(n, k, generator_polynome, message):
    # n должно быть больше k
    if (n <= k): return
    # Соответствует умножению на x^(n-k)
    shifted_message = message << n - k
    # Вычисляем синдром
    sindrome = xor_division_remainder(shifted_message, generator_polynome)
    # Производим конкатенацию его со сдвинутым сообщением
    shifted_message += sindrome
    # Возвращаем закодированный сигнал
    return shifted_message

def cyclicCode_decode(generator_polynome, message):
    pass

def makeBinaryArray(number):
    i = 0
    result = np.array([0])
    result = np.delete(result, 0)
    while number > 0:
        if (number % 2):
            result = np.append(result, i)
        i += 1
        number //= 2
    return result

def deleteCommonValues(a, b):
    i = 0
    while i < len(a):
        val = a[i]
        if val in b:
            b = np.delete(b, np.where(b == val))
            a = np.delete(a, i)
            i -= 1
        i += 1
    return a, b

def addArr(a, b):
    for i in range(len(b)):
        if b[i] not in a:
            a = np.append(a, b[i])
    return a

def xor_division_remainder(numerator, denominator):
    # Если числитель нулевой, сразу возвращаем 0
    if numerator == 0: return 0
    # Поместим номера разрядов числа, равных 1, в массив
    # Таким образом получим номера степеней полученных многочленов в одном массиве
    # Например: 10 = 1010 -> [3, 1]
    numer = makeBinaryArray(numerator)
    denom = makeBinaryArray(denominator)
    # Найдем остаток от деления числа n на число d
    # Итерируем до тех пор, пока степень многочлена d не станет меньше
    max_d = max(denom)
    while max(numer) >= max_d:
        # Часть ответа. Она нам не важна, т.к. нужен лишь остаток
        # Число, на которое нужно умножить знаменатель, чтобы потом вычесть его из числителя
        mult = max(numer) - max(denom)
        # В случае степеней процесс умножения превращается в сложения, прибавляем нужную степень
        curr = denom + mult
        # Следующие действия связаны со спецификой сложения в кольце
        # Удаляем из массивов общие элементы
        numer, curr = deleteCommonValues(numer, curr)
        # Отставшиеся в знаменателе значения возвращаем в числитель
        numer = addArr(numer, curr)
        # Если за итерацию числитель стал равен 0, значит делится без остатка
        if len(numer) == 0 and len(curr) == 0:
            break
    if len(numer) == 0:
        return 0
    result = 0
    # Формируем результат, помечая единицами соответствующие разряды
    for i in numer:
        result += 1 << i
    return result

def shiftLast(a):
    return (a - 1) ^ ((a^(a-1)) >> 2)

def add1AfterLast(a):
    return a | ( ((a^(a-1)) + 1) >> 2 )

def firstCombination(n, k):
    return ((1 << k) - 1) << (n - k)

def nextCombination(a):
    if (a & (a + 1)) == 0 :
        return 0

    if (a & 1):
        return add1AfterLast( nextCombination(a >> 1) << 1 )
    else:
        return shiftLast(a)

def combination(n, k):
    number = firstCombination(n, k)
    while (number != 0):
        yield number
        number = nextCombination(number)