from decimal import ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP
import enum
from math import dist
import sys
sys.stdin = open("input.txt", "rt")



# avg = 0
# distance = []
# minDis = float('inf')

# for x in b:
#     avg += x
# avg = round(avg/a)

# for i in range(len(b)):
#     if b[i] < avg:
#         b[i] = 0
#     if abs(b[i] - avg):
#         distance.append(abs(b[i]-avg))
#     if distance[i] < minDis:
#         minDis = distance[i]

# print(minDis)
# for i in range(len(b)):
#     if minDis == b[i]:
#         print(b[i])

# --- 포기
# 하단은 답안
a = int(input())
b = list(map(int, input().split()))
ave = ROUND_HALF_UP(sum(b)/a)
min = float('inf')

for index, x in enumerate(b): # a의 배열 값에 0부터 시작하는 인덱스를 매겨주는 함수
    tmp = abs(x-ave)
    if tmp < min :
        min = tmp
        score = x
        res = index+1
    elif tmp == min : # 만약 평균값과의 거리가 동일하다면
        if x > score : # x를 score에 할당하기 전에 비교한다. 이 경우는 score에 x가 할당되어 있고 현재 비교되는 x는 index+1인 x다
            score = x
            res = index+1
print(ave, res)

# 