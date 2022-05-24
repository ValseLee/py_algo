# a = [0] * 3
# print(a) 1차원 리스트 생성

a = [[0]*3 for _ in range(3)]
# print(a) # 2차원 리스트 생성
# x,y 좌표를 찍을 수 있는 평면 표로 이해하면 좋다
# 행 번호와 열 번호
# print()

a[0][1] = 1
a[1][1] = 2
# print(a)

for x in a: # X 는 여기서 행 번호라는 점 명심
    print(x)
    # 3개의 행을 각각 출력(이 출력은 리스트에 담겨있다)

for x in a: # 행에 접근하고
    for y in x: # 열에 접근하여
        print(y, end=' ') # 값을 출력
    print()