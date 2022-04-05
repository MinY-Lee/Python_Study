# 프로그래머스 사이트에서 작동해야 정상작동됨(이전 입력 코드가 있음)
# https://programmers.co.kr/learn/courses/30/lessons/60061

# 현재 구조물이 정상인지 체크하면서 하기

# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y -1, 0] in answer:
                continue
            return False    # 아니라면 거짓(False) 반환
        elif stuff == 1:    # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y-1, 0] in answer or [x + 1, y - 1, 0] in answer or([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False    # 아니라면 거짓(False) 반환
    return True