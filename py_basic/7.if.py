x = -3
if x >= 0:
    print('Lucky')
    if x % 3 == 0:
        print("3의 배수")
    if x % 2 == 0:
        print("2의 배수")
    if x < 10:
        print("10 이하 자연수")
else:
    print("nope")