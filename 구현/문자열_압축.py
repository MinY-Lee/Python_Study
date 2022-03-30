# 프로그래머스 사이트에서 테스트해야 정상 동작함.
# 문자열 길이의 절반까지 나눌 수 있으므로 1개 이상~문자열의 절반까지 순서대로 나눠본다
s = input()
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]    # 앞에서부터 step만큼의 문자열 추출
        count = 1



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

