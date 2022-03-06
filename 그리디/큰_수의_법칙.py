# n, m, k를 공백 구분해 입력
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
# 큰 순으로 정렬
data.sort(reverse=True)

# 가장 큰 수
one = data[0]
# 두번째로 큰 수
two = data[1]

i = 1
result = 0
savek = k

while i <= m:
    if k > 0:
        result += one
        k -= 1
    else :
        result += two
        k = savek
        
    i += 1

print(result)


#########################################################
# 밑에는 수학적 논리로 푸는 방법 = 덩어리로 묶어서 생각해보기

# 큰 수가 더해지는 횟수
count = int(m/(k+1))*k + m%(k+1)

result2 = 0
result2 += count * one + (m-count) * two
print(result2)