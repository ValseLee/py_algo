/*
 Permutation == 순열
 수열의 순서를 뒤섞어서 만드는 수열.
 파이썬은.. permutation 내장 메소드가 있다..
 꼬우면.. 아시죵..?

 아래의 permutations는 레이 웬더리히의 코드를 참고했다.
*/

import Foundation

let n = Int(readLine()!)!
let lineArray = readLine()!.split(separator: " ").map { Int($0)! }
var array = [[Int]]()
var answer = -1

func solution(_ n: Int, _ array: [[Int]]) -> Int {
    for i in array {
        var sum = 0
        for j in 0 ..< n - 1 {
            sum += abs(i[j] - i[j + 1])
        }
        if answer < sum {
            answer = sum
        }
    }
    return answer
}

func permuteWirth(_ arr: [Int], _ n: Int) {
    if n == 0 {
        array.append(arr)
    } else {
        var arr = arr
        permuteWirth(arr, n - 1)

        for i in 0 ..< n {
            arr.swapAt(i, n)
            permuteWirth(arr, n - 1)
            arr.swapAt(i, n)
        }
    }
}

permuteWirth(lineArray, n - 1)
print(solution(n, array))
// print(solution(n, lineArray)) // 6