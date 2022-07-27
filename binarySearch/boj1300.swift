/*
 1. 어떤 수가 배열 내의 k번째 수라면?
    - 그 수는 배열 내에서 자기보다 작은 수를 K-1개, 큰 수를 arr.count - K개 이하로 갖는다.
 
 2. 만약 n = 5, k = 17인 예제를 풀어본다면?
 가장 작은 수는 1(low), 가장 큰 수는 25다(high).
 중간 값은 13이다(mid).

 3. 13보다 작은 수는 몇 개이고 큰 수는 몇 개인지 확인한다.
 만약 13이 17번째 수라면 작은 수는 16개 이하, 큰 수는 8개 이하여야 한다.
 작은 수 : 5 + 5 + 4 + 3 + 2  == 19
 큰 수  : 0 + 0 + 1 + 2 + 3  == 6
 13은 자기 자신보다 작은 수가 너무 많기 때문에 13보다 작은 수를 기준으로 삼아야 한다.
 그래서 13보다 작은 12 부터 다시 시작한다.

 4. 1과 12의 중간값은 6이다(버림).
 만약 6이 17번째 수라면 작은 수는 16개 이하, 큰 수는 8개 이하여야 한다.
 작은 수 : 5 + 2 + 1 + 0 + 0 == 8
 큰 수  : 0 + 2 + 3 + 4 + 4 == 13
 6은 자기 자신보다 큰 수가 너무 많다. 6보다 수가 커져야 할 것

 5. 7과 12 사이의 중간값은 9이다(버림).
 9의 경우는 아래와 같다.
 작은 수 : 5 + 4 + 2 + 2 + 1 == 14
 큰 수 : 0 + 1 + 2 + 3 + 4 == 10
 9도 자기 자신보다 큰 수가 더 많기 때문에 9보다 커져야 한다.

 6. 10과 12 사이의 중간값은 11이다.
 11의 경우는 아래와 같다.
 작은 수 : 5 + 5 + 3 + 2 + 2 == 17
 큰 수 : 0 + 0 + 3 + 2 + 2 == 7
 11도 조건을 만족하지 않는다.

 답은 10

 ---
 배열 없이 특정 수보다 작은 수가 몇 개인지 어떻게 알 수 있을까?
 무식하게 filter{ $0 < x }.count 이렇게 하지 말자.
 i행에서 i행의 숫자는 j만큼 곱해진다.
 i, 2i, 3i, 4i ... i * j ...
 x는 i와 j를 곱한 수보다 작아야 한다. ==> ij < x
 그런데 j가 계속 커질 수도 있으니, n보다도 작아야 한다.
 따라서 i번째 행에서 x보다 작은 수의 갯수는 min(n, (x - 1) / i)개가 된다.
 x에서 1을 빼는 건 ij == x 를 배제해야 하기 때문
 
 더 큰 수는 어떨까
 i번째 행에서 x보다 큰 수의 갯수는 n - min(n, x / i)개다.
 왜? n - (i행에서 x보다 작은 수의 갯수) 연산을 실행한 결과가 x보다 큰 개수일 테니까.
*/

import Foundation

let n = Int(readLine()!)!
let k = Int(readLine()!)!

var smallerCnt = 0
var biggerCnt = 0

func getSmaller(num: Int) -> Int {
    smallerCnt = 0
    for i in 1 ... n {
        smallerCnt += min(n, (num - 1) / i)
    }
    return smallerCnt
}

func getBigger(num: Int) -> Int {
    biggerCnt = 0
    for i in 1 ... n {
        biggerCnt += (n - min(n, num / i))
    }
    return biggerCnt
}

func solution(_ n: Int, _ k: Int) -> Int {
    var low = 1
    var high = n * n
    var answer = 0

    while low <= high {
        var mid = (low + high) / 2
        smallerCnt = getSmaller(num: mid)
        biggerCnt = getBigger(num: mid)

        if smallerCnt > k - 1 {
            high = mid - 1
        } else if biggerCnt > n * n - k {
            low = mid + 1
        } else {
            answer = mid
            break
        }
    }
    return answer
}

print(solution(n, k))
// 5, 17 // 10
// 3, 7 // 6