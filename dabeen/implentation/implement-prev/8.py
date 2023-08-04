#8. 문자열 재정렬
#join() 함수 등 야매로 푼거같다..
val = input()
arr = []
cnt = 0

for v in val:
    if v.isalpha():
        arr.append(v)
    else:
        print(v)
        cnt+=int(v)

arr.sort()  #정렬(오름차순)
arr = ''.join(arr)

print(arr,str(cnt),sep='')