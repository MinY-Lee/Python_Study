# 모든 음식을 우선순위 큐에 삽입. (음식 시간, 음식 번호)의 튜플 형태로 삽입.
# 우선순위 큐를 구현하기 위해 headpq를 이용
# 프로그래머스 홈페이지에서 실행해야 제대로 된 실행
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

# 나중에 다시 풀어보기

from xxlimited import foo
import headpq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        headpq.heappush(q, (food_times[i], i + 1))
        
    sum_value = 0   # 먹기 위해 사용한 시간
    previous = 0    # 직전에 다 먹은 음식 시간
    
    length = len(food_times)    # 남은 음식의 개수
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정
        
    # 남은 음식 중에서 몇 번째 음식인지 확인해 출력
    result = sorted(q, key = lambda x: x[1])    # 음식의 번호 기준으로 정렬
    return sesult[(k - sum_value) % length][1]