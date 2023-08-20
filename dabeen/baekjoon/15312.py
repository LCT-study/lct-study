#이름궁합 (구현)
# 10 이상이면 뒷자리 수만 출력
# 알파벳은 무조건 대문자로만

arr = input()
brr = input()

alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
res = []
tmp = []

#문자를 숫자로 변환 (처음만)
for i in range(len(arr)):
    res.append(alpha[ord(arr[i]) - 65])
    res.append(alpha[ord(brr[i]) - 65])

while len(res) > 2:
    for i in range(len(res)-1):
        tmp.append((res[i]+res[i+1]) % 10)
    res = tmp
    tmp = []


print('%d%d'%(res[0],res[1]))