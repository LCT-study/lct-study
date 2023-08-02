def zip_str(strings):
    min_length= 1001
    word = ""
    for s in strings:
        s = s.replace("1","")
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
        for j in range(0, len(s), i):
            #print(i, j, s[j:j+i], count)
            string = s[j:j+i]
            if temp:
                if temp[-1]!=string:
                    data+=(str(count)+temp.pop())
                    count=1
                    temp.append(string)
                else:
                    count+=1
            else:
                temp.append(string)
        if temp:
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