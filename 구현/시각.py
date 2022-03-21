# 시간 입력받기
hour = int(input())
result = 0

# 시간, 분, 초 모두 반복
for i in range (hour + 1):
    for j in range (60):
        for k in range(60):
            # 3이 들어있는 경우 result + 1
            # 3시 5분 33초의 경우 '30533'으로 만들어서 3이 있는지 확인
            # +말고 or을 사용하면 ('3' in str(i) or str(J)) j는 모두 집계되므로 이렇게 쓰고싶으면 
            # ('3' in str(i) or '3' in str(J)) 이렇게 써야 함
            if '3' in str(i) + str(j) + str(k):
                result += 1
                
print(result)