import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
M = list(map(int, input().split()))
res = set() # res에 값을 여러번 넣어도 단 한 번만 실행됨 = 중복 제거

# 3번을 뽑아서 3번 더해야 한다.
# -> 1회 시행될 때, 1번, 2번, 3번을 동시에 계산해야 한다.
for i in range(N):
    for j in range(i+1, N):
        for l in range(j+1, N):
            res.add(M[i]+M[j]+M[l])
res = list(res)
res.sort(reverse=True)
print(res[K-1])