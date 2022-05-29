# for i in range(10):
#     print(i) # 0 ~ 9

# for i in range(10,0,-1):
#     print(i)

# j = 1
# while True:
#     print(j)
#     j += 1
#     if j == 15:
#         break

for i in range(1, 11):
    if i % 2 == 0:
        continue
    # print(i)

for i in range(1, 11):
    print(i)
    if i == 5:
        break
else: # else 는 break 당하지 않은 for loop에 추가적으로 반복문을 달아줄 때 쓴다.
    print(11)