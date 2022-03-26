# 맵 크기 입력받기
import turtle

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성해 0으로 초기화
# 리스트 컴프리헨션을 사용한다(이차원 배열의 초기화의 경우 반드시!)
d = [[0] * m for _ in range(n)]     # _는 변수의 값을 무시해도 괜찮을 때 사용("hello"를 5번 출력하는 경우 등)
# 현재 캐릭터의 X좌표, Y좌표, 방향 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1     # 현재 좌표는 방문했다고 처리

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction    # global이란? 해당 변수를 전역변수로 사용 할 것임을 선언
    direction -= 1
    if direction == -1:
        direction = 3   # 여기 이해 잘 안감 -> 오른쪽이 아니라 왼쪽으로 회전이기 때문에 3(오오오 해야 왼 이랑 똑같음)
        
# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:   # 가 보지 않은 칸이고 갈 수 있는 칸이면
        d[nx][ny] = 1   # 이동했다고 바꾸기
        x = nx  # x 좌표 이동
        y = ny  # y 좌표 이동
        count += 1      # 이동한 횟수 추가
        turn_time = 0   # 회전 한 횟수
        continue
    
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:  # 모든 방향 한번씩 다 돌은 것
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
    
# 정답 출력    
print(count)

# 완전히 틀린 문제
# 2차원 배열의 경우 꼭! 리스트 컴프리헨션 사용하는거 기억하기!
# 2차원 배열 좀 더 이해하기 + 문제를 좀 더 이해하기