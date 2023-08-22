
# 균형잡힌 문자열 index 반환 함수
def getBalancePoint(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i]=="(":
            count+=1
        else:
            count-=1
        if count==0:
            return i
    
# 올바른 문자열 여부 확인 함수
def isRight(arr):
    stack = []
    for i in arr:
        if i=='(':
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

# 문자열 괄호 방향 뒤집는 함수        
def flip(arr):
    flipped=""
    for i in arr:
        if i == "(":
            flipped+=")"
        else:
            flipped+="("
    return flipped


def solution(p):
    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    answer = ""
    if p=="":
        return answer

    # 2. 균형잡힌 괄호 문자열 분리
    idx = getBalancePoint(p)
    u,v = p[:idx+1],p[idx+1:]
    
    # 3. u가 올바른 문자열인 경우, v에 대해서 1단계부터 다시 수행
    if isRight(u):
        # 3-1. 수행 결과를 다시 문자열 u에 이어 붙임
        answer = u+solution(v)
        
    else:# 4. 문자열 u가 올바른 문자열이 아니라면 다음의 과정 수행
        answer = ""
        # 4-1. 빈 문자열에 첫번째 문자로 (  붙임
        answer += "("
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 이어 붙임
        answer += solution(v)
        # 4-3. ) 붙임
        answer += ")" 
        # 4-4. u의 첫번째와 마지막 문자를 제거하고,
        # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
        answer += flip(u[1:-1])
    # 4-5. 생성된 문자열 반환
    return answer
    

