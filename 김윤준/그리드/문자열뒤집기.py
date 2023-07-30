#"0101100010010"

#1과 0의 개수중 더 작은수가 횟수다.

#11110011


S = str(input())
num = 0

for i in range(len(S)):
    if(S[i] == S[i+1]):
        num += 0

print(min(num))


