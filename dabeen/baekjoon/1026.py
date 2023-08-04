#1026 보물 (그리디)
#goal: arr을 재배열 및 큰 수는 무조건 작은수랑 곱하게

n = int(input())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
res =[]

arr.sort(reverse=True) #내림차순
brr.sort() #오름차순
print(arr, brr)

for a,b in zip(arr,brr):
    res.append(a*b)
print(sum(res))