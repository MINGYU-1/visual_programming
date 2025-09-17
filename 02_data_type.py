# 연산
x= True
y= False
x, y = True, False

print(x and y)
print( x or y)
print( not x)
print(1 < 1)
print(1 <= 1)
print(1 > 1)
print( 1 == 1)
print( 1 != 1)

a = 10 
b = 4
c = 1

print(a ** b)
print(a // b) # 몫 연산
print(a % b) # 나머지 연산


# 컴퓨터에서 숫자를 처리하는 것이기 때문에 시험에는 나오지 않는다. 
x = 3 #11
y = 2 #10
print(x & y)

print(x | y) # or 연산

print(x ^ y) # xor 연산

print(x << y) # 11 << 2 = 1100(비트를 옆으로 미는 연산)

print(~x)
## 실수의 계산
# - 2진법을 이용해서 구하기 떄문에 실수를 정확하게 표시하지 못한다. 굳이 그럴필요가 없기때문에 그러지 않았다.
# - 가수부를 구해서 수치를 이용해서 확인하면 더 와닿는다. 
# - 우연하게도 표시할 수 있는 수인 경우에만 표시가능하다고 생각하면 된다. 실수는 표현하기 어렵다고 생각하면 된다. 
a = 1.2
b = 1.1
c = 1.0
print(a + b)
print(a - b) # 0.09999999999999 2진수이기떄문에 생기는 문제이다.
print(a * b)
print(a / b) # 1.0999999999999
a = '123'
b = "123"
c = '''123''' # 문단 사용가능
d = """123"""
a,b,c,d
print(a * 3)
b = """'''a'''"""
print(b)