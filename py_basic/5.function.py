def add(a, b):
    c = a+b
    print(c)
add(1,2)
add(5,7)

def add2(a, b):
    c = a+b
    return c
print(add2(3,2))

def add3(a,b):
    c = a+b
    d = a-b
    return c, d # 여러값을 동시에 리턴할 수 있고 이럴 땐 튜플로
print(add3(2,3))

# --- 소수만 출력해보자
a = [12, 13, 7, 9, 19]

def isPrime(x):
    for i in range(2, x):
        if x % i ==0:
            return False
    return x

for x in a:
    if isPrime(x):
        print(x, end=' ')