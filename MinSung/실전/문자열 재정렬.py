s = input()

alpa = []
n = 0

for i in s:
    if i.isalpha():     #값이 알파벳이면 리스트에 추가
        alpa.append(i)
    else:
        n = n + int(i)  #값이 숫자면 더해줌
alpa.sort() #알파벳 오름차순 정렬

if n != 0:  #숫자가 하나라도 있으면 맨 뒤에 문자로 삽입
    alpa.append(str(n))

for i in alpa:     #리스트를 출력
    print(i, end='')