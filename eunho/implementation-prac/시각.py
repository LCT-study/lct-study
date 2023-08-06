# chapter4 구현 실전[4-2]
# input : 5 => output : 11475

def calculate(num):
    #03, 13, 23, ... 53 => 총 15개
    return num * ((15 * 60) + (45 * 15))

n = int(input())
count_3 = 0
answer = 0
hour_3_list = [3, 13, 23]

for hour in hour_3_list:
    if n - hour < 0: break
    answer += 3600 # 시간에 3이 포함되어 있으면, 3600++
    count_3 += 1 # 시간에 3이 포함된 수 개수를 세기

answer += calculate((n + 1) - count_3)
print(answer)