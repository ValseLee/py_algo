# 익명함수 = 람다함수 = 람다표현식
def plus_one(x):
    return x +1
plus_one(2)
print(plus_one(2))

# 아래처럼 활용
plus_two = lambda x: x +2
# x가 매개변수
# 할당하여 사용한다(익명함수)
print(plus_two(2))

# 왜 람다를 쓸까?
a = [1, 2, 3, 4]
print(list(map(plus_one, a)))
# map(x, y) = x 는 함수, y엔 리스트를 받는다.
# y의 데이터들에 접근해서 함수를 작동하고,
# 상단의 print는 그 값을 다시 list로 감싸준다.
print(map(plus_one, a))

# map처럼 함수를 인자로 받는 자리에 곧바로 함수를 쓸 수 있다
print(list(map(lambda x: x+1, a)))

# 알고에서는 sort할 때 주로 람다 활용