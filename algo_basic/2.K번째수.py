import sys
sys.stdin = open("input.txt", "rt")

T = int(input())

for t in range(T):
    n, s, e, k = map(int,input().split())
    a = list(map(int, input().split()))
    # print(a) # 1번 케이스의 자료, 2번 케이스의 자료를 순서대로 확인 가능
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))
