# n, m을 공백으로 구분해 입력
# 행과 열 입력받기
n, m = map(int, input().split())
answer = 0
current = 0

# 행의 수 만큼 반복
for i in range(n):
    # 현재 입력받은 행에서 가장 작은 숫자
    current = min(map(int, input().split()))
    if current>answer:
        answer = current
        # 이전 행과 비교해 큰걸 채택
        
print(answer)

#######################
# 또 다른 방법의 경우
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # 가장 작은 수 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result)   # 최종 출력