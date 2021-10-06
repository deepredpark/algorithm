i = 1
while True:
    L, P, V = map(int, input().split())
    if not L: break
    result = (V // P) * L + min(V % P, L)
    print("Case {}:" .format(i), result)
    i += 1
