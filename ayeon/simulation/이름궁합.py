import sys
input = sys.stdin.readline

name1 = list(input().strip())
name2 = list(input().strip())
count = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 
1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

start = []
char_start = ord("A")
for idx in range(len(name1)):
    chr1 = count[ord(name1[idx])-char_start]
    chr2 = count[ord(name2[idx])-char_start]
    #print(chr1, chr2)
    start.append(chr1)
    start.append(chr2)
#print(start)

while True:
    temp = []
    for idx in range(len(start)-1):
        op1 = start[idx]
        op2 = start[idx+1]
        value = op1+op2
        temp.append(int(str(value)[-1]))
    if len(temp)==2:
        print("".join(list(map(str,temp))))
        break
    #print(temp)
    start=temp

    