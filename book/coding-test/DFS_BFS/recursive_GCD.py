#GCD 유클리드 호제법

def GCD(a, b):
    if a % b ==0:
        return b
    else:
        return GCD(b, a % b)

print(GCD(192, 162))
