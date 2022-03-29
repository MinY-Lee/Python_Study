# 문자열 입력받기
data = input()


result = 0

for i in range(1, len(data)//2):
    for j in range(0, len(data)-i):
        i += j
        print(i, j)
        if j==0:
            slic = data[j:i]
        else:
            if slic == data[j:i]:
                result += 1
                slice = data[j:i]
                
print(result)