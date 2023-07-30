S = str(input())

S = list(S)

sum = int(S[0])
for i in range(len(S)-1):
    if(S[i+1] != '0' and S[i+1] != '1' and sum != 0 and sum !=1): # 곱할때 손해가 나오는 경우를 제외했을 때
        print(sum, " x ", int(S[i+1]))
        sum *= int(S[i+1])
    else: # 곱할때 손해가 나왔을 경우 더해줌
        print(sum, " + ", int(S[i + 1]))
        sum += int(S[i+1])
    print("[", sum, "]")
