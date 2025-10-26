import Foundation

func solution(_ citations:[Int]) -> Int {
    let arr = citations.sorted(by: >)
    for i in 0..<arr.count {
        if arr[i] < i+1 {
            return i
        }
    }
    return arr.count
}