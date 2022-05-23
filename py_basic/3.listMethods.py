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