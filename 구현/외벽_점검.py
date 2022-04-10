# https://programmers.co.kr/learn/courses/30/lessons/60062  에서 기본 코드 제공
from itertools import permutations
# permutations = ex) 8P8 = 8!
# 순열(permutations)을 사용해 할 수 있다-> 친구를 나열하는 모든 경우의 수를 각각 확인해 몇명 배치하면 되는지
# 원으로 되어 있다면 계산을 편하게 하기 위해 일자로 바꿔주기(길이 2배해서)
# 완전 탐색 아이디어로 풀 수 있다!

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)    # weak의 마지막에 추가해주기
    answer = len(dist) + 1  # 투압할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대해 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1   # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]     # 여기가 왜인지 이해가 안감 좀 더 공부해서 마저 완성하기!