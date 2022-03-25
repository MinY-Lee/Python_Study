# 데이터 입력받기(현재 위치)
location = input()
line = int(location[1])
row = ord(location[0])-ord('a') + 1
# ord를 사용하면 해당 문자의 아스키 코드값을 받아올 수 있음

# 움직일 수 있는 경우의 수
moves = [(-2,1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
# 실제 움직일 수 있는 가짓수
result = 0
for move in moves:
    next_line = line + move[1]
    next_row = row + move[0]
    if next_row >= 1 and next_row <= 8 and next_line >= 1 and next_line <= 8:
        result += 1

print(result)