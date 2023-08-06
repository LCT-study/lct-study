def create_zip(count, chunk, result):
    
    if count>=2:
        result +=str(count)+chunk
    else:
        result+=chunk
    
    return result
    

def solution(s):
    min_len = len(s)
    for unit in range(1, (len(s)//2)+1):

        # 결과 문자열
        result = ""    

        # 첫 탐색 단위
        chunk = s[0:unit]

        # 동일한 탐색 단위의 개수
        count = 1

        # 탐색 인덱스를 탐색 단위만큼 증가시키며, 이전 탐색 단위와 비교
        for idx in range(unit, len(s), unit):

            # 현재 탐색 단위를 슬라이싱
            now = s[idx:idx+unit]

            # 현재 탐색 단위가 이전 탐색 단위와 같다면
            if (now == chunk):
                count += 1
            # 현재 탐색 단위가 이전 탐색 단위와 다르다면
            else:
                result = create_zip(count, chunk, result)
                chunk = now
                count = 1

        # 남아있는 문자열에 대해 처리
        result = create_zip(count, chunk, result)

        # 탐색 단위별로 압축 문자열의 길이를 비교해, 최소 압축 문자열의 길이를 저장
        min_len = min(min_len, len(result))

    return min_len





input1 = "aabbaccc"
input2 = "ababcdcdababcdcd"
input3 = "abcabcdede"
input4 = "abcabcabcabcdededededede"
input5 = "xababcdcdababcdcd"
inputs = [input1, input2, input3, input4, input5]
#inputs = [input4]

for s in inputs:
    print(solution(s))