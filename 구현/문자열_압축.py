# 프로그래머스 사이트에서 테스트해야 정상 동작함.
# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 길이의 절반까지 나눌 수 있으므로 1개 이상~문자열의 절반까지 순서대로 나눠본다

def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]    # 앞에서부터 step만큼의 문자열 추출
        count = 1   # count = 압축 횟수
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:   # j부터 j + step 까지가 앞에와 같은지
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]    # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
        
    return answer
                
# ==============================================================================

# 다른 방법으로 할 수 있을지 생각해보기

# # 문자열 입력받기
# data = input()
# result = 0

# for i in range(1, len(data)//2):
#     for j in range(0, len(data)-i):
#         i += j
#         print(i, j)
#         if j==0:
#             slic = data[j:i]
#         else:
#             if slic == data[j:i]:
#                 result += 1
#                 slice = data[j:i]
                
# print(result)

