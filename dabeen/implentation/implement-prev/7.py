#럭키 스트레이트

arr = input()
n=len(arr)//2
arr_f = arr[:n]
arr_b = arr[n:]

front = sum([int(x) for x in arr_f])
back = sum([int(x) for x in arr_b])

if front != back:
    print("READY")
else:
    print("LUCKY")