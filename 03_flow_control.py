# 예제1
a,b,c = 1,2,3
# a = int(input())
# b = int(input())
# c = int(input())
if c < a:
    print(a)
elif c > b:
    print(b)
elif c in range(a,b+1):
    print((a+b)/2)

#예제2
repeat = False
grade = 'A+'
match grade:
    case 'A+' if not repeat:
        print(4.5)
    case 'A+' if repeat:
        print(4)
    case 'A':
        print(4)
    case 'B+':
        print(3.5)
    case 'B':
        print(3)
    case 'C+':
        print(2.5)    
    case 'C':
        print(2)
    case 'D+':
        print(1.5)
    case 'D':
        print(1)
    case 'F':
        print(0)

#예제3
#value값 판별
value = 105
i = 2
while i <value:
    if value % i == 0:
        print("소수가 아닙니다.")
        break
    i += 1
else:
    print("소수입니다.")
#예제4
sum = 0
for number in range(1, 101):
    #소수 판별하기
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            break
    if i == 1:
        is_prime = False
    if is_prime:
        sum += number
print(sum)
#예제5
number = 50
for i in range(10):
    guess = input("맞춰보세요:")
    guess = int(guess)

    if guess == number:
        print('Win')
        break
    elif guess >number:
        print('Down')
    elif guess < number:
        print('Up')
else:
    print("You lose")



