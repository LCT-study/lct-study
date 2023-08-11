n = input()

left = 0
right = 0

for i in range(len(n) // 2):    #왼쪽 반
    left = left + int(n[i])
for i in range(len(n) // 2, len(n)):    #오른쪽 반
    right = right + int(n[i])
if left == right:
    print('LUCKY')
else:
    print('READY')    