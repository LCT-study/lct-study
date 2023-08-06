# input : K1KA5CB7, output : ABCKK13

unsorted_list = list(input())
num_set = set('0123456789')
sum = 0
alpha_list = []

for compo in unsorted_list:
    if compo in num_set: sum += int(compo)
    else: alpha_list.append(compo)

sorted = sorted(alpha_list)
sorted.append(sum)

print(*sorted, sep='')

