#문자열 압축(다시 풀기)
#프로그래머스

def solutions(s):
    answer = len(s)

    #1부터 시작해서 길이 제한은 문자열의 반까지(len(s)//2+1)
    for step in range(1, len(s)//2+1):
        compressed ="" #문자열을 담는 곳
        prev = s[0:step]  #앞에서부터 step(1부터,,)만큼의 문자열 추출
        cnt = 1

        #단위 만큼 증가시키면서 얼마나 전 문자열과 겹치는지 비교
        for j in range(step, len(s), step): #step단위 만큼

            # aab일경우 a, 뒤에a를 비교 a == a, a!=b 하나씩 비교
            if prev == s[j: j+step]:
                cnt+=1
            else:
                compressed +=str(cnt) + prev if cnt>=2 else prev
                prev = s[j: j+step] #초기화
                cnt = 1

        #남은 문자열들 처리
        compressed += str(cnt) + prev if cnt>= 2 else prev
        
        #만들어진 압축 문자열의 길이가 가장 짧은 것을 채택
        answer = min(answer,len(compressed)) 
        #answer와 만들어진 문자열 길이 비교 및 계속 리뉴얼함