#2. 왕실의 나이트 (다시 풀어보기: 어려움)
#내 생각: 찐 구현대로 풀었는데 좀 더 고려하면서 풀면 좋을거 같다
n = input()

x,y = 0,0 #현 좌표의 위치(x,y)

y = int(ord(n[0])) - int(ord('a')) + 1
x = int(n[1])
cnt =0 #경우의 수

print(x,y)

if (y+2) <= 8 :
    if x+1 <=8 :
        cnt+=1
    if x-1>=1:
        cnt+=1
if (y-2) >= 1:
    if x+1 <=8 :
        cnt+=1
    if x-1>=1:
        cnt+=1

if (x+2)<=8 :
    if y+1 <=8 :
        cnt+=1
    if y-1>=1:
        cnt += 1

if (x-2)>=1:
    if y+1 <=8 :
        cnt+=1
    if y-1>=1:
        cnt += 1
print(cnt)