import sys
sys.stdin = open("input.txt","rt")
print()

# 어떤 자연수 n,q 가 있고 p를 q로 나눌때 나머지가 0이면 q는 p의 약수
# 이 중, K가 주어질 때, q중 K번째로 작은 수?
# 약수 없으면 -1 출력

n,k = map(int, input().split())
count = 0

for i in range(1,n+1):
    if n % i == 0:
        count += 1
    if count == k:
        print(i)
        break
else:
    print(-1)