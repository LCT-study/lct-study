
# 주어진 문자열 p가 올바른 괄호 문자열인지 판단하는 함수
def is_correct_parentheses(p):
    stack = []
    for ch in p:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def transform(p):
    if not p:
        return ""

    left, right = 0, 0
    u, v = "", ""
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break

    if is_correct_parentheses(u):
        return u + transform(v)
    else:
        new_p = "(" + transform(v) + ")"
        for ch in u[1:-1]:
            if ch == '(':
                new_p += ')'
            else:
                new_p += '('
        return new_p

p = input()
result = transform(p)
print(result)
