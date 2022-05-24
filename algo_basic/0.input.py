# 값 하나를 받기
a = input()

# 값 2개를 받기
a, b = input().split() # 이대로 받으면 스트링 형태

a, b = map(int, input().split) # 받은 숫자들을 전부 정수로 받는다.