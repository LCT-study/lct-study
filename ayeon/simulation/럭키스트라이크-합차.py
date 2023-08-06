import sys
input = sys.stdin.readline

n = list(map(int, input()))
length = len(n)
answer = 0

for i in range(length//2):
    answer+=n[i] # 왼쪽 값을 더하고

for i in range(length//2, length):
    answer-=n[i] # 오른쪽 값을 빼고
    
if answer == 0: # 왼쪽과 오른쪽이 같으면 같은 값을 빼고 더한 것임 
    print("LUCKY")
else:
    print("READY")