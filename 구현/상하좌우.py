# 데이터의 수 입력
from shutil import move


n = int(input())

# 좌우상하 입력(LRUD)
data = list(input().split())

xline = 1
yline = 1
x = 1
y = 1
print(data[2])
for i in range(0, len(data)):
    x, y = xline, yline
    
    if data[i]=="L":
        x -= 1
    elif data[i]=="R":
        x += 1
    elif data[i]=="U":
        y -= 1
    elif data[i]=="D":
        y += 1
    # 범위 밖을 벗어나는 경우
    if x < 1 or y < 1 or x > n or y > n:
        continue
    else:
        xline, yline = x, y
    
    
print('x좌표: ', xline, ' y좌표: ', yline)


###########################################
# # 책에 나온 정답풀이
# x, y = 1, 1
# plans = input().split()

# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# # 이동 계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         # L, R, U, D와 같은거 찾기(어디로 이동하는지)
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#             print(plan)
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
    
# print(x, y)