import sys

# n 입력(수의 개수) 한 줄씩 입력
n = int(sys.stdin.readline())
# 연산자 리스트
numbers = list(map(int, input().split()))
# 각 연산자의 개수
add, sub, mul, div = map(int, sys.stdin.readline().split())

# 최솟값, 최댓값 초기화 (int형 숫자 10억을 대입)
min_value = int(1e9)
max_value = -int(1e9)

# 깊이 우선 탐색 DFS
def dfs(i, now):    #i= 현재까지 사용한 연산자의 개수, now= 현재까지 계산된 수식의 값
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:  #dfs 함수에서 현재까지 사용한 연산자의 개수 i가 전체 연산자의 개수 n과 같아졌을 때
        min_value = min(min_value, now)             #최소, 최대값 업데이트
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1    #현재 사용한 덧셈 연산자의 개수를 1 감소시킴
            dfs(i + 1, now + numbers[i])    #i+1번째 수와 더해진 결과를 now에 더해줌
            add += 1    #dfs 함수의 실행이 끝나면 다시 add += 1을 통해 덧셈 연산자의 개수를 원래대로
                        #복구시킴 이렇게 함으로써, 현재 사용한 덧셈 연산자의 개수를 기억하면서 
                        # 모든 가능한 연산자 조합을 시도할 수 있다.
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / numbers[i])) # 나눌 때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, numbers[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)