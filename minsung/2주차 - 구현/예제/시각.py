n = int(input()) #시간 입력 받기

count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            #시각 안에 '3'이 포함되어 있으면 카운트 증가
            if '3' in str(i) + str(j) + str(k): #각 시각을 문자열로 변환하여
                count = count + 1               # 3이 포함되는지 확인
print(count)                