N, M = map(int, input().split())

board = [[0] * M for i in range(N)] # 2차원 배열 선언 함수

list_add = []

min_a = 0 # 더 큰수가 저장되게끔 비교할 변수
min_b = 0 # 저장될 변수

for i in range(N):
    list_add = list(map(int, input().split())) # 열씩 배열을 입력받음
    if(min_a < min(list_add)) : # '기존 최소값' 보다 '입력받은 배열' 최소값이 클 경우 변수에 저장
        min_b = min(list_add)
    min_a = min(list_add) # 다음 열 비교시 입력받은 배열 최소값을 기존 최소값으로 설정
    for j in range(M):
        board[i][j] = list_add[j] # 배열에 입력받은 배열 저장

print(min_b)
