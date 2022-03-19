# 데이터의 수 입력
n = int(input())

# 좌우상하 입력(LRUD)
data = list(input().split())

xline = 1
yline = 1
x = 1
y = 1
print(data[2])
for i in range(0, len(data)-1):
    x, y = xline, yline
    
    if data[i]=="L":
        x -= 1
    elif data[i]=="R":
        x += 1
    elif data[i]=="U":
        y -= 1
    elif data[i]=="D":
        y += 1
    
    if x < 1 or y < 1 or x > n or y > n:
        continue
    else:
        xline, yline = x, y
    print('x좌표: ', xline, ' y좌표: ', yline)
    
    
print('x좌표: ', xline, ' y좌표: ', yline)
    