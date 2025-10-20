# 예제1
import math
def determinant(a,b,c):
    D = b**2 - 4 * a * c
    if D >0:
        d = math.sqrt(D)
        return (-b+d)/(2*a), (-b-d)/(2*a)
    if D == 0:
        return -b/(2*a)
    if D < 0:
        return None
print(determinant(3,1,2))

# 예제2
def 소수(n):
    if n <= 1:
        return "소수가 아니다."
    i = 2
    is_prime2 = True
    while i * i <= n:
        if n % i == 0:
            is_prime2 = False
            break
        i += 1
    if is_prime2:
        return "소수"
def is_prime(n):
    count = 0
    for i in range(n+1):
        if 소수(i) == "소수":
            count += 1
    return count
print(is_prime(10))

#예제 3
import math
def f(x, a, b, c):
    return a * x**2 + b * x + c

def g(x, a, b, c):
    return a * math.sin(b * x) + c

a, b, c, n = map(float, input().split())

result = f(g(n, a, b, c), a, b, c)
print(result)

#예제4
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

x = float(input().strip())

x_rounded = round(x, 4)

frac = abs(x_rounded) - int(abs(x_rounded))
n = int(round(frac * 1000))
if n >= 1000:   
    n = 999
best = None
best_diff = 10**9
for p in range(2, 1000):
    if is_prime(p):
        d = abs(p - n)
        if d < best_diff or (d == best_diff and p < best):
            best_diff = d
            best = p

print(best)


#예제5
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):     # n번 반복
        print(a, end=' ')
        a, b = b, a + b
fibonacci(int(input()))
