import Foundation

func solution(_ numbers:[Int]) -> Int {
    let correct: Set<Int> = [0,1,2,3,4,5,6,7,8,9]
    let missing = correct.subtracting(numbers)
    return missing.reduce(0,+)
}