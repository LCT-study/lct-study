# input : 123402
# output : LUCKY

num_list = list(input())
front_sum = 0
back_sum = 0

for i in range(len(num_list)):
    if i < len(num_list) // 2:
        front_sum += int(num_list[i])
    else: back_sum += int(num_list[i])

if front_sum == back_sum:
    print("LUCKY")
else: print("READY")