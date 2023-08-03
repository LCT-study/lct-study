# 가장 작은 문자열압축 찾는 함수
def zip_str(strings):
    min_length= 1001
    word = ""
    for s in strings:
        if min_length > len(s):
            #print(s, len(s))
            min_length = len(s)
            word = s
    return min_length, word

def solution(s):
    answer = []
    for i in range(1,(len(s)+1)//2+1):
        temp = []
        count = 1
        data = ""

        # 쪼개서 연속된 갯수 세기
        for j in range(0, len(s), i):
            #print(i, j, s[j:j+i], count)
            string = s[j:j+i]
            if temp:
                if temp[-1]!=string:
                    if count==1: # 갯수가 1개면 숫자 없이 
                        data +=temp.pop()
                    else: # 갯수가 1개가 아닌 경우 
                        data+=(str(count)+temp.pop())
                    count=1
                    temp.append(string)
                else:
                    count+=1
            else:
                temp.append(string)
        
        # 마지막 남은 조각에 대한 처리 
        if temp:
            if count==1:
                data +=temp.pop()
            else:
                data+=(str(count)+temp.pop())
        answer.append(data)
        
    length, word = zip_str(answer)
    return length
    

    
input1 = "aabbaccc"
input2 = "ababcdcdababcdcd"
input3 = "abcabcdede"
input4 = "abcabcabcabcdededededede"
input5 = "xababcdcdababcdcd"
inputs = [input1, input2, input3, input4, input5]
#inputs = [input4]

for s in inputs:
    print(solution(s))