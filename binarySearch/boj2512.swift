/*
1. 상한액의 최소값과 최대값은 몇인가?
    0 ~ 주어지는 요구 예산 중 최대값
    예제에서는 평균이 0 + 150 / 2 == 75
    이 평균값이 이제 상한액 기준값이 된다.
2. 그럼 이 평균을 부서의 수만큼 더해본다.
    75 * 4 = 300
    예산보다 적다.
3. 가능한 상한액을 높인다.
    다시 75와 150의 평균을 구해본다.
    (75 + 150) / 2 == 112.5 ==> 112
4. 각 부서별 금액과 비교해서 이 상한액과 값을 잘 비교해서 실제 수령할 값을 잘 처리할 것.
5. 112 + 110 + 112 + 112 = 446
6. 다시 상한액을 높인다.
    112와 150의 평균을 구한다.
    (112 + 150) / 2 == 131
7. 이번엔 상한액과 요구 예산 총합이 가능 예산보다 커졌다.
8. 그럼 상한액은 112와 131 사이에 있을 것.
9. 이것을 반복한다. 
*/

import Foundation

let n = Int(readLine()!)!
let lineArray: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
let availableMoney = Int(readLine()!)!

func solution(_ n: Int, _ arr: [Int], _ availableMoney: Int) -> Int {
    var down = 0
    var high = arr.max()!
    var mid = (down + high) / 2
    var answer = 0

     while down <= high {    
        let total = arr.map { a in 
            a > mid ? mid : a
        }.reduce(0) {
            a, b in a + b
        }

        if total <= availableMoney {
            down = mid + 1
            answer = mid
        } else {
            high = mid - 1
        }
        mid = (down + high) / 2
        print(total, down, mid, high)
    }

    return answer
}

print(solution(n, lineArray, availableMoney))
print(solution(4, [120, 110, 140, 150], 485)) // 127
print(solution(5, [70, 80, 30, 40, 100], 450)) // 100
