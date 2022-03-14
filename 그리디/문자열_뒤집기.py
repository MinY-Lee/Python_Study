# 0과 1로 이루어진 문자열(ex|0001100)을 모두 1이나 모두 0으로 바꾸는 것 중 더 적게 바꾸는 경우
# 데이터 입력받기
data = input()

num0 = 0
num1 = 0

# 첫 번째 원소 처리
if(data[0]=='0'):
    num1 += 1
else:
    num0 += 1
    
# 두번째 이후 원소 처리
for i in range(0, len(data)-1):
    if(data[i] != data[i+1]):
        # 1로 바꾸는 경우
        if(data[i]=='1'):
            num1 += 1
        
        # if(data[i]=='0'):
        #     num0 += 1
        # 이게 좀 더 간편한 코드
        else:
            num0 += 1
            
# if(num0<num1):
#     print(num0)
# else:
#     print(num1)

print(min(num0, num1))