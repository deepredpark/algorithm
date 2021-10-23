# Review 2
# greedy : 현재 상황에서 가장 좋은 것만 선택하는 방법
# note! : 햔재의 선택이 나중에 미칠 영향에 대해 고려하지 않는다.
# 특정한 문제를 만났을 때, 단순히 현재 상황에서
# 가장 좋아보이는 것만 선택해도 문제를 풀 수 있는지 파악 필요!

# greedy review 1
# page315 볼링공 고르기 9 min
n, m = map(int, input().split())
array = list(map(int, input().split()))

count = 0
for i in range(n - 1):
  A = array[i]
  for j in range(i+1, n):
    B = array[j]
    if A != B:
      count += 1
print(count)

#page316 무지의 먹방 라이브
def solution(food_times, k):
    answer = 0
    n = len(food_times)
    time = 0
    mini_count = 0
    while mini_count < n:
      if answer != n and food_times[answer] == 0:
        answer += 1
        mini_count += 1
        continue
      elif answer != n:
        food_times[answer] -= 1
        time += 1
        answer += 1
      if answer == n:
        answer = 0
        mini_count = 0
      if time == k:
        return answer + 1
    return -1 

print(solution([3, 1, 2], 5))
