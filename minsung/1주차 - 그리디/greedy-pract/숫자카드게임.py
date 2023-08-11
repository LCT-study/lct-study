n, m = map(int, input().split())
max_Num = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_Num = min(data)              #data 안에 가장 작은 수 찾기 
    max_Num = max(min_Num, max_Num)  #가장 작은 수들에서 가장 큰 수 찾기
print(max_Num)
    

'''
for i in range(1, n + 1):   # 2중 for문으로 랜덤 숫자 출력
    for j in range(1, m + 1):
        print(random.randint(1, 10), end = ' ')
    print()
'''