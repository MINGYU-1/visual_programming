# 5번
import random
user_value = input('수를 입력하세요')
user_value = int(user_value)
result = set()
for i in range(user_value):
    random_value = random.randint(1,100)
    result.add(random_value)
print(f"{len(result)}이 크기입니다.")
# 6번
import random
result_value = input("로또 번호를 입력해주세요:")
result_value = result_value.split()
user_value = list(result_value)
user_lotto = set()
for value in user_value:
    user_lotto.add(int(value))

lotto_pool = []
for value in range(1,46):
    lotto_pool.append(value)
random.shuffle(lotto_pool)
chosen_lotto = set(lotto_pool[:6])

print(f'{len(user_lotto & chosen_lotto)}'+'개 맞았습니다.')
# 7번
import random

# 집합 n과 m 정의
n = set(range(1, 101))
m = set(range(1, 11))

count = 0
for _ in range(100):
    n_prime = set()
    while len(n_prime) < 5:
        n_prime.add(random.randint(1, 100))
    if n_prime.issubset(m):
        count += 1

print(f">>> {count}번")
 # 8번

store_items = {}

print("물건 이름과 금액을 5번 입력하세요 (예: 아이스크림 500):")

for _ in range(5):
    item_input = input().split()
    item_name = item_input[0]
    item_price = int(item_input[1])
    
    store_items[item_name] = item_price

total_price = sum(store_items.values())

print(f">>> {total_price}원")

#9번
try:
    allowed_duplicates = int(input("허용 중복수를 입력하세요: "))
except ValueError:
    print("숫자를 입력해주세요.")
    exit()

try:
    numbers_input = input("값을 입력하세요: ").split()
    if len(numbers_input) != 10:
        print("10개의 값을 입력해야 합니다.")
        exit()
    numbers = [int(n) for n in numbers_input]
except ValueError:
    print("모든 값은 정수여야 합니다.")
    exit()
counts = {}
for num in numbers:
    counts[num] = counts.get(num, 0) + 1

duplicates = []
for num, count in counts.items():
    if count > allowed_duplicates:
        duplicates.append(str(num))
if duplicates:
    print(">>> 중복된 수:", ' '.join(duplicates))
else:
    print(">>> 중복된 수가 없습니다.")