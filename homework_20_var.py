from utils import cyclic_code_encode
from utils import xor_division_remainder
from utils import combination
from math import factorial

# Параметры циклического кодирования
n = 15
k = 11
gVector = 0b10011

# Поступившая информация
informationVector = 0b11111010001

# Кодирование информации
encoded = cyclic_code_encode(n, k, gVector, informationVector)

len = 32
print("="*len)
print(f"{'i':>3} {'Cin':>8} {'n0':>8} {'c0':>10}")
print("="*len)


for k in range(1, n + 1):
    errors = 0  # nErrors
    for error in combination(n, k):
        errVector = encoded ^ error
        sindrome = xor_division_remainder(errVector, gVector)
        if sindrome != 0:
            errors += 1
    comb_count = factorial(n) / factorial(k) / factorial(n - k)
    c0 = errors/comb_count
    print(f"{k:3} {comb_count:8} {errors: 8} {c0 * 100:>8.2f} %")
    print("-"*len)
