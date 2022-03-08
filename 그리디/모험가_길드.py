# 그룹을 최대한 많이 만들 수 있는 경우의 수
# 전체 인원 수 입력
from sklearn.utils import resample


n = int(input())

# 공포치 입력받기
fear = list(map(int, input().split()))
# 오름차순 정렬
fear.sort()
result = 0  # 총 그룹의 수

count = 0   # 현재 그룹에 포험된 모험가의 수

for i in fear:  # 공포도가 낮은 것부터 하나씩 확인
    count += 1  # 현재 그룹에 해당 모험가 추가
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0   # 현재 그룹에 포함된 모험가의 수 초기화
        
print(result)