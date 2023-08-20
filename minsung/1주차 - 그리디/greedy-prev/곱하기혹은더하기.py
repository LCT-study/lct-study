'''s = input()
result = int(s[0])

for i in range(1, len(s)):
    # 두 수  중에서 하나라도 0, 1인 경우, 더하기 수행
    num = int(s[i])
    if num <= 1 or result <= 1:
        result = result + num
    else:
        result = result * num
print(result)       
        '''

      

#s_input = input()
# 1 0 7 2 4
#s = input()
s = list(map(int, input().split()))

sum = 0
for i in range(len(s)-1):
    if s[i] == 0:       #s[i]이 0일 때 바로 뒤의 숫자와 더함
        sum = sum + s[i] + s[i + 1]
    if s[i] == 1:       # s[i]이 1일 때 바로 뒤의 숫자와 곱함 
        sum = sum + s[i] * s[i + 1]
        if s[i + 1] == 0:   #그 때 뒤의 숫자가 0일때 더함
            sum = sum + s[i] + s[i + 1]
    if s[i] >= 2:
        sum = sum * s[i + 1]    #s[i]가 2보다 크거나 같으면 뒤의 숫자와 곱함
        if s[i + 1] == 0 or 1:  #뒤의 숫자가 0이거나 1이면 더함
            sum = sum + s[i] + s[i + 1]
print(sum)   

        
        
'''        
s_input = input()
# 1 0 7 2 4
#s = input()

s = list(s_input)

sum = int(s[0])
for i in range(len(s)-1):
    if s[i] == "0":       #s[i]이 0일 때 바로 뒤의 숫자와 더함
        sum = sum + int(s[i + 1])
        print("1", sum)
    elif s[i] == "1":       # s[i]이 1일 때 바로 뒤의 숫자와 곱함
        sum = sum  + int(s[i + 1])
        print("2", sum)
        if s[i + 1] == 0:   #그 때 뒤의 숫자가 0일때 더함
            sum = sum  + int(s[i + 1])
            print("3", sum)
    elif s[i] >= "2":
        sum = sum * int(s[i + 1])
        print("4", sum)        #s[i]가 2보다 크거나 같으면 뒤의 숫자와 곱함
        if s[i + 1] == "0" or  s[i + 1] == "1":  #뒤의 숫자가 0이거나 1이면 더함
            sum = sum  + int(s[i + 1])
            print("5", sum)
print(sum)

'''




