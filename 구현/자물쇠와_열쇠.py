# https://programmers.co.kr/learn/courses/30/lessons/60059  에서 해야 정상 작동
# 완전 탐색을 이용해 문제 풀기
# 자물쇠의 9배 크기의 새로운 리스트 만들기(가운데가 자물쇠)
# 옮겨가면서 자물쇠+열쇠의 모든 부분이 1이 되는 곳 찾기

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])   # 열 길이 계산
    result = [[0] * n for _ in range(m)]    # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result
# 이해가 잘 가지 않는다면 리스트 그려서 90도 하나씩 해보기

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3    # new_lock은 원래 lock이 가운데에 있는 9배 크기이므로 가로세로가 3배, 따라서 //3을 해야 원래 lock 길이가 나옴
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

