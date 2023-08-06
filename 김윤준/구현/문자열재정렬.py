String = input()
Char = list()
num = 0

for i in String:
    if i.isdigit(): # 숫자면 그 숫자를 num에 저장
        num += int(i)
    else:  # 아니면 문자니 Char에 문자 저장
        Char.append(i)

Char.sort()
if num != 0: #숫자가 하나라도 존재하면
    Char.append(str(num))

print("".join(Char)) # 매개변수로 들어온 리스트에 있는 요소 하나하나 합쳐서 하나의 문자열로 바꿔줌