# 문자열 입력받기
s = input()
# 리스트로 해야 알파벳순으로 정리 가능
result = []
sum = 0

# 문자 하나씩 확인
for x in s:
    # 알파벳인 경우 리스트에 삽입
    # .isalpha() 를 사용하면 알파벳이지 아닌지 구분 가능
    if x.isalpha():
        # 알파벳인 경우 append(변수) 를 사용해 추가(append는 리스트 맨 뒤에 삽입해줌)
        result.append(x)
    else:
        # 숫자인 경우 int로 바꿔 더하기
        sum += int(x)

# abc순으로 정렬하기        
result.sort()
# "구분자".join(리스트)   를 사용해 리스트를 문자열로 합쳐주기
answer = "".join(result) + str(sum)
print(answer)

# 생각은 맞게 했으나 모르는 함수(append, join, isalpha) 가 있어 찾아봐야 했음
# 다음에 다시 한번 더 풀어보기!