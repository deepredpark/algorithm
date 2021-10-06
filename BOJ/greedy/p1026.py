#BOJ 1026
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
B.reverse()

result = 0
for i in range(n):
    result += A[i] * B[i]

print(result)