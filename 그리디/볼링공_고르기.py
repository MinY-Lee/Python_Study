# 서로 다른 무게의 볼링공을 고르는 경우의 수
# 입력받기
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# 같은 무게의 공이 몇개인지
count = 1
result = 0

for i in range(0,len(data)-1):
    # 다음 공의 무게가 다른 경우
    if(data[i] != data[i+1]):
        # 같은 무게의 공이 있는 경우
        if(count!=1):
            result += (len(data) - i - 1) * count
        # 같은 무게의 공이 없는 경우
        else:
            result += len(data)-i-1
        count = 1
    # 다음 공의 무게가 같은 경우
    else:
        count += 1
        
        
        
# # 책에서 재시한 해결책
# # 1부터 10까지의 무게를 담을 수 있는 리스트 생성
# array = [0] * 11

# for x in data:
#     # 각 무게에 해당하는 볼링공의 개수 카운트
#     array[x] += 1
    
# # 1부터 m까지의 각 무게에 대해 처리
# for i in range(1, m+1):
#     n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#     result += array[i] * n # B가 선택하는 경우의 수와 곱하기
        
    
    
    
print(result)