# BOJ 1037 약수
n = int(input())
divisors = list(map(int, input().split()))
divisors.sort()
print(divisors[0] * divisors[-1])
