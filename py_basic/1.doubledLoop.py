
# for i in range(5):
#     print('i:', i, sep='', end=' -> ')
#     for j in range(5): # i가 0일 때 5번 돌고, 1일 때 5번...
#         print('j:', j, sep='', end=' ')
#     print()

for i in range(5):
    for j in range(5):
        print("*", end=' ')
    print()

for i in range(6):
    for j in range(5):
        print("*" * i, end=' ')
    print()

for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()

