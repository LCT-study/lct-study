data = input()

num = ['1','2','3','4','5','6','7','8','9']
num_list = list()
alpha_list = list()

for d in data:
    if d in num:
        num_list.append(int(d))
    else:
        alpha_list.append(d)

alpha_list.sort()
alpha_list.append(str(sum(num_list)))
for a in alpha_list:
    print(a,end='')