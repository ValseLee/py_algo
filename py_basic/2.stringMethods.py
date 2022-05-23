msg = "It is Time"

print(msg.upper()) # 문자열은 변하지 않고 변화만 시킨다.
print(msg.lower())
print(msg)
tmp = msg.upper()
print(tmp)
print(tmp.find("T")) # index를 리턴
print(tmp.count('T')) # T가 몇개니?
print(msg[:2]) # slice 기능 / 문자열의 index 이전까지 추출 -> 'it' 리턴 // 'it '를 리턴하는 게 아님!
print(msg[3:5]) # 3,4 index 리턴 // 슬라이스될 때는 이상 ~ 미만 으로 리턴된다는 걸 명심
print(len(msg)) # 글자 수 리턴 = 10

for i in range(len(msg)): # i는 0부터 9까지 돌게 될 것
    print(msg[i], end='')
print()

for x in msg: # 문자열에 직접 차례로 접근 // 인덱싱 하지 않아도 된다구
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():
        print(x, end='\n') # 대문자만 출력, islower 도 있다

for x in msg:
    if x.isalpha(): # 알파벳만 리턴
        print(x, end=' ')

print('\n')

tmp2 = 'AZ'
for x in tmp2:
    print(ord(x)) # ASCII Number return / A = 65, Z = 90

tmp3 = 'az'
for x in tmp3:
    print(ord(x)) # a = 97, z = 122

tmp4 = 65
print(chr(tmp4)) # Int를 chr 하면 아스키 숫자에 대응하는 알파벳을 리턴