#page130
def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i+1, "번째 재귀 함수를호출합니다.")
    recursive_function(i+1)
    print(i, "번째 재귀함수를 종료합니다.")
recursive_function(1)

#factorial example add.
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
