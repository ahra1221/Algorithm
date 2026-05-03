import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var answer = [Int]()
    for com in commands {
        let i = com[0], j = com[1], k = com[2]
        let subArr = Array(array[i-1..<j]).sorted()
        answer.append(subArr[k-1])
    }
    return answer
}