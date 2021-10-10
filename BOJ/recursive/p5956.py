def cow_count(n, m):
  if n % 2 == 0 or m % 2 == 0:
    return 0

  return 1 + 4 * cow_count((n-1)/2, (m-1)/2)

n, m = map(int, input().split())
print(cow_count(n, m))
