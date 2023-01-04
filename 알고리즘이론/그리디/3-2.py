# 큰 수의 법칙

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

# 입력받은 수 순서대로 정리하기
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:     # 총 m번 돌아가기
    for i in range(k):      # 가장 큰 수를 k번 더해주기
        if m == 0 :
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second        # 두 번째로 큰 수 한번 더해주기
    m -= 1
# True일 동안은 계속 돌아가기 때문에 두번째 큰 수 한번 더해주고 다시 제일 큰 수를 k번 더해주는 식으로 간다

print(result)