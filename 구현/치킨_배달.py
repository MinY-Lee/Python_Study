# 조합!!!! 을 생각해서 라이브러리 가져올 수 있느냐가 가장 큰 아이디어!!!!
from itertools import combinations  # 조합 라이브러리 - 전체 N개 중 M개 고르기 = nCm

# 도시 크기, 치킨집 수 입력받기
# 이건 생각했음
n, m = map(int, input().split())

chicken, house = [], []

# 도시 구조 입력받기
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))    # 일반 집
        elif data[c] == 2:
            chicken.append((r, c))  # 치킨 집
        
# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = 1e9  # e는 10의 거듭제곱을 나타냄 -> 1 X 10의 9승
        print(temp)
        for cx, cy in candidate:
            # 치킨집 까지의 거리
            temp = min(temp, abs(hx - cx) + abs(hy - cy))   # abs() 함수: 절댓값
            # 왜 temp가 1e9인가 궁금했는데 최솟값을 찾기 위함이어서 그럼
            # 13Cm의 값의 최대가 100,000이므로 이것 이상이면 올바른 값이 나올 듯.
            # 밑의 result도 비슷한 의미같음.
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
    
print(result)