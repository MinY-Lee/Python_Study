# 숫자 입력받기
# n이 k로 나누어떨어지는 경우만 나눌 수 있다. 아니면 n-1
# n이 1이 되는 최소 횟수 구하기
n, k = map(int, input().split())
count = 0

num = n

while n>1 :
    if n % k == 0:
        n = n//k
    else:
        n-=1
    count += 1
    
print(count)

#########################
# 예시 답안 - 시간이 적게 걸리게 해 보자!
result = 0
while True:
    # num을 k의 배수로 바꿔주고 그만큼 결과 더하기
    target = (num//k) * k
    result += (num - target)
    num = target
    # num이 k보다 작은 경우
    if num < k:
        break
    # k로 나누기
    result +=1
    num //= k
    
# 마지막 계산(k이하이므로 빼는 횟수 더하기)
result += (num-1)
print(result)