#참고: https://alpyrithm.tistory.com/134 풀이 2

n_cities = int(input())
loads = list(map(int, input().split()))
L_charges = list(map(int, input().split()))

charge = L_charges[0]
result = 0
for i in range(n_cities-1):
    if charge > L_charges[i]:
        charge = L_charges[i]
    result += charge * loads[i]

print(result)
