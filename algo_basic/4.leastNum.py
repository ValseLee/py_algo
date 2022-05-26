# 이 배열의 가장 작은 숫자 인덱스를 리턴

arr = [5,3,7,9,2,5,2,6]
arrMin = float('inf') # 가장 큰 값으로 초기화
for i in range(len(arr)):
    if arr[i] < arrMin: # 등호가 없다는 걸 유의해
        arrMin = arr[i]
    # 무한 arrMin과 arr[i]를 계속 비교하고,
    # 무한 값에 arr[i]를 한번 대입한 다음
    # 그 값을 비교
    # 왜 무한대를 넣는가?
    # 어떤 숫자든 무한보다는 작으니까 -> 첫 비교를 위해
print(arr.index(arrMin)) # 4 

### 물론 무한으로 초기화하지 않고 0번인덱스로 초기화해도 상관은 없다