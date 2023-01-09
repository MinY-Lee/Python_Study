# 1이 될 때까지

n, m = map(int, input().split())
count = 0
while True:
    if n % m == 0:
        n = n / m
    else:
        n -= 1
    count += 1

    if n == 1 :
        break

print(count)

# 다른 방법: n이 m의 배수가 되도록 먼저 빼기