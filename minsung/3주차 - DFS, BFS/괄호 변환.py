# 균형잡힌 괄호 문자열의 인덱스를 반환하는 함수
def check_balance_idx(p):
    # 왼쪽 괄호의 개수
    count = 0
    for i in range(len(p)):
        if (p[i] == '('):
            count += 1
        else:
            count -= 1
        if (count == 0):
            return i

# 올바른 괄호 문자열인지 판단하는 함수
def check_right(p):
    # 왼쪽 괄호의 개수
    count = 0
    for i in range(len(p)):
        if (p[i] == '('):
            count += 1
        else:
            # 왼쪽 괄호가 없는 상태에서 오른쪽 괄호가 등장한 경우
            if (count == 0):
                return False
            count -= 1
    return True

def solution(p):

    # 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if (p == ''):
        return ''

    # 문자열을 두 균형잡힌 괄호 문자열 u, v로 분리
    balance_idx = check_balance_idx(p)

    u = p[:balance_idx+1]
    v = p[balance_idx+1:]

    # u가 올바른 괄호 문자열인지 판단
    if (check_right(u) == True):
        return u + solution(v)
    else:

        # u의 첫번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 발향을 뒤집는 작업
        temp = ""
        for element in u[1:-1]:
            if (element == '('):
                temp += ')'
            else:
                temp += '('

        return '(' + solution(v) + ')' + temp