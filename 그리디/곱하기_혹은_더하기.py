# 입력된 숫자의 각 자리 숫자를 더하거나 곱해서 가장 큰 수로 만들기
# 숫자 입력받기
data = input()

# 입력받은 숫자의 첫번째 가져오기
result = int(data[0])

# 숫자가 끝날 때 까지 반복
# 둘 중 하나가 0이나 1인 경우 덧셈을 하는게 더 큰 수를 만들 수 있으므로 조건으로 걸기
# 처음에 둘 다 1보다 큰 경우로 했으나 둘 중 하나가 1 이하일 경우가 더 나음!!
for i in range(1, len(data)):
    if result <= 1 or int(data[i]) <= 1:
        result += int(data[i])
    else:
        result *= int(data[i])
        
print("정답은", result)