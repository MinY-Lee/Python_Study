# 예제 3-1 거스름돈

n = 1260
count = 0

# 큰 단위 화폐부터 거슬러주기
coin = [500, 100, 50, 10]

for rest in coin:
    count += n  // rest
    n %= rest   # 나머지

print(count)