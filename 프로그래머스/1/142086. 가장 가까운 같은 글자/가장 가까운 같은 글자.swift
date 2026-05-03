import Foundation

func solution(_ s:String) -> [Int] {
    var answer = Array(repeating:-1, count:s.count)
    var dict: [Character: Int] = [:]
    for (idx, c) in s.enumerated() {
        if let val = dict[c] {
            answer[idx] = (idx-val)
        } else {
            answer[idx] = -1
        }
        dict[c] = idx
    }
    return answer
}