# 예제1
user_input = input("두수를 입력하세요: ")
a,b = map(float, user_input.split(','))
print((a,b))
# 예제2
coord= (1,1),(3,3),(5,5),(7,7),(9,9)
sum_x = 0
sum_y = 0
for i in range(len(coord)):
    sum_x += coord[i][0]
    sum_y += coord[i][1]
center_x = sum_x /len(coord)
center_y = sum_y /len(coord)
for i in range(len(coord)):
    print(((coord[i][0]-center_x)**2+ (coord[i][1]-center_y)**2)**(1/2))

#예제3
a = [2, 6, -3, 4, 0]
sorted(a)[0]
a = [1,3,4,3,]
a.pop(1)

#예제4
coord = []
for i in range(5):
    user_input = input(str(i)+'번째 수를 입력하시오')
    a,b = user_input.split(',')
    a,b = float(a),float(b)
    coord.append((a,b))

user_input = input('기준점을 입력하시오')
a,b = user_input.split(',')
a,b = float(a),float(b)
t = (a,b)

for i in range(5):
    if coord[i][0] == t[0] and coord[i][1] == t[1]:
        coord.pop(i)
distances = []
for i in range(len(coord)):
    distance = ((t[0]- coord[i][0])**2+ (t[1]-coord[i][1])**2)**(1/2)
    distances.append(distance)

if distances:
    print(min(distances))
else:
    print("기준점 제외 후 남은 좌표가 없습니다.")