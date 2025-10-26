import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var ans: Set<Int> = []
    for i in 0..<numbers.count-1{
        for j in i+1..<numbers.count {
            let sum = numbers[i] + numbers[j]
            ans.insert(sum)
        }
    }
    return Array(ans).sorted()
}