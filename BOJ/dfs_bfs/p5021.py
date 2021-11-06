# BOJ p5021 왕위 계승
# DFS, BFS, Topological_sort는 그래프문제 상황에 맞게 풀기!!
# ★그래프면 이건 꼭 Topological이다! 이런게 없다는 뜻, DFS, BFS, Brute forcing 항상 같이 고려하자!
# reference = https://velog.io/@leehj8896/%EB%B0%B1%EC%A4%80-5021%EB%B2%88-%EC%99%95%EC%9C%84-%EA%B3%84%EC%8A%B9
import sys
input = sys.stdin.readline

n_child, n_candidate = map(int, input().split())
king = input().rstrip()
parents_tree = {}
candidates = []
for _ in range(n_child):
  child, parent1, parent2 = input().split()
  for name in [child, parent1, parent2]:
    if name not in parents_tree:
      parents_tree[name] = []
    parents_tree[child] = [parent1, parent2]
for _ in range(n_candidate):
  candidates.append(input().rstrip())
  
def blood_dfs(name):
  if name == king:
    return 1
  if name not in parents_tree:
    return 0
  if not parents_tree[name]:
    return 0
  return (blood_dfs(parents_tree[name][0]) + blood_dfs(parents_tree[name][1])) / 2

max_value = -1
max_name = None
for candidate in candidates:
  blood = blood_dfs(candidate)
  if blood > max_value:
    max_value = blood
    max_name = candidate

print(max_name)
