import random as r
from tkinter.tix import Tree

# b=list()
# print(b)

a=[1,2,3,4,5]
# print(a)
# print(a[0])

# b=list(range(1,11))
# print(b)

# c = a+b
# print(c)

a.append(6)
print(a)

a.insert(3, 7) # 특정 index에 오도록 7 넣기
print(a)

a.pop()
print(a) # stack out
# pop은 인덱스를 지정해서 뺄 수도 있다.

a.remove(4) # 값을 찾아서 제거
print(a)

print(a.index(5)) # 값을 찾고 인덱스 리턴

a = list(range(1, 11))
print(a)

print(sum(a)) # 리스트의 값들을 전부 합하기
print(max(a)) # 최대값 리턴

r.shuffle(a)
print(a) # print 인자로 shuffle을 넣으면 none이 나오네..?

# sort
a.sort()
print(a)
a.sort(reverse = True)
print(a)
a.clear()
print(a)

a = [23, 12 ,36, 53, 19]
print(a[:3])
print(a[1:4])

print(len(a))

for i in range(len(a)):
    print(i, end=' ') # 0~4
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ') # 위와 동일한 아웃풋
print()

for x in a:
     if x % 2 == 1:
         print(x, end=' ') # 홀수 출력
print()

for x in enumerate(a): # tuple로 출력
    print(x) # 인덱스 번호와 밸류를 동시에 뽑아낸다

# 튜플 : 일차원 리스트
b = (1, 2, 3, 4, 5)
print(b[0])
# b[0] = 7 # Tuple은 값 변경 불가
# 왜? 튜플은 저 덩어리가 메모리에 그대로 저장되기 때문에?

for x in enumerate(a):
    print(x[0], x[1]) # tuple 을 데이터 벗겨내서 출력
print()
print()

for index, value in enumerate(a):
    print(index, value)

# 
#
if all(50 > x for x in a): # for 가 a를 돌리고 x에 할당
    # x에 할당된 모든 값들을 all 함수의 조건과 비교한다.
    # 모두가 참일 때! print한다.
    print("true")
else:
    print("false")
print()

if any(11 > x for x in a):
    # any는 단 하나라도 만족한다면 참을 리턴한다
    print("yes")
else:
    print('no') 