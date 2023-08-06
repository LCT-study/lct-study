n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
sum = 0

B_index_dict = {B[i] : i for i in range(n)}
B_sorted = sorted(B, reverse= True)
for i in range(n):
    idx = B_index_dict[B_sorted[i]]
    sum += B[idx] * A[i]
print(sum)