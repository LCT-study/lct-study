import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
i = arr[0] # 가장 큰 수 
j = arr[1] # 두번째로 큰 수 

# 가장 큰 수 더해지는 횟수
i_count = int(m/(k+1))*k + m%(k+1) 

# 두번째로 큰 수 더해지는 횟수 
j_count = m - i_count

answer = i_count * i + j_count*j

print(answer)