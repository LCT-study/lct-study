import sys
input = sys.stdin.readline

arr =list(input().strip()) 
alpha = []
num = []


for i in arr:
    if i.isalpha():
        alpha.append(i)
        #print(i, "alpha")
    elif i.isdigit():
        num.append(int(i))
        #print(i,"num")
        
answer = sorted(alpha)+[str(sum(num))]
print("".join(answer))

"""
K1KA5CB7
ABCKK13
"""

"""
AJKDLSI412K4JSJ9D
ADDIJJJKKLSS20
"""