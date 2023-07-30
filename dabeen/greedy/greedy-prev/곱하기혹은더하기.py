#곱하기 혹은 더하기
s = input()
res = 0

for val in(s):
    v = int(val)
    if v == 0:
        continue
    if res != 0:
        res *= v
        continue
    res+=v


print(res)