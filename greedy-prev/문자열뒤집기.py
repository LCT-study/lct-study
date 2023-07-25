import sys
input = sys.stdin.readline

n = input().strip()
prev = n[0]
count=0

for i in n[1:]:
    if prev!=i:
        count+=1
    prev = i
    
print((count+1)//2)