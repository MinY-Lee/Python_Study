# 숫자 받기
n = input()
# 전체 길이
length = len(n)
result = 0

# 왼쪽 부분 계산
for i in range(length//2):
    result += int(n[i])
    
# 오른쪽 부분 계산
for i in range(length//2, length):
    result -= int(n[i])
    
if result == 0:
    print("LUCKY")
else:
    print("READY")