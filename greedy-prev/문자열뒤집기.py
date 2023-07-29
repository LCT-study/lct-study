import sys
input = sys.stdin.readline

# 0001100
# 1 

n= input().strip()
# print(n)

# 전부 0으로 바꾸는 경우 =  전부 1로 바꾸는 경우 = 0
count0 = count1 = 0

# 첫 원소 처리
if n[0]=="1": 
    count0+=1
else:
    count1+=1

for i in range(len(n)-1):
    if n[i]!=n[i+1]: #다음 원소가 현재 원소와 다른 경우
        if n[i+1]=="1": # 다음 수가 1인 경우
            count0+=1
        else: # 다음 수가 0인 경우
            count1+=1
            
print(min(count1, count0))
        