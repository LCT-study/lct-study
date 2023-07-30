import time

# 내가 쓴 코드
start_time = time.time()
N, M, K = input().split()
l = [N, M, K] # 5 8 3

data = []
data = input().split() # 2 4 5 4 6
max_data = max(data) # 가장 큰 수 저장

sum = 0 # 더해줄 변수
count = 0 # 더해주는 횟수 카운트
bool = 0 # 3번 더해지고 더해지는 수 바꿀 시 다른 수로 바꾸는 조건 변수.

for i in range(int(l[1])) :
    if(count == int(l[2])) : # 최대 K번 더할 수 있음
        if(bool == 0):
            count = int(l[2]) - 1
            data.remove(max(data)) # 초과하여 더해진 수 삭제
            bool = 1
        elif(bool == 1): # 0 초기화로 다시 기존에 입력받은 최대값으로 더해짐.
            count = 0
            bool = 0
            data.append(max_data)
    count += 1
    print(sum, "+", int(max(data)))
    sum += int(max(data))

end_time = time.time()
print(sum, end_time - start_time)

# 정답 : 반복문 없이
