# 보드 크기 입력받기
n = int(input())
# 사과 갯수 입력받기
apple = int(input())

# 리스트 컴프리헨션을 사용한다(이차원 배열의 초기화의 경우 반드시!)
data = [[0] * (n + 1) for _ in range(n + 1)]    # 맵 정보
# =================================================== 일단 위에까지 생각은 성공함
# 밑에부터는 틀린부분

info = []   # 방향 회전 정보

# 맵 정보(사과가 있는 곳은 1로 표시)
for _ in range(apple):
    a, b = map(int, input().split())
    data[a][b] = 1
    
# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()      # 초와 이동할 방향 입력받기
    info.append((int(x), c))    # append(): 리스트 마지막에 요소 추가
    
# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)   방향 정해서 이동시 dx, dy 사용이 좋다!!!!!!!!!!!!!
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":    # 왼쪽으로 도는거면
        direction = (direction -1) % 4      # 왜..?? 이 부분 이해가 안감
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    direction = 0   # 처음에는 동쪽을 보고 있음
    time = 0    # 시작한 뒤에 지난 '초' 시간
    index = 0   # 다음에 회전할 정보
    q = [(x, y)]    # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        