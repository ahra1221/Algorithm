import Foundation

func solution(_ citations:[Int]) -> Int {
    var citation = citations.sorted(by: >)
    
    var h = 0
    for i in 0..<citation.count {
        if citation[i] >= i + 1 { h = i + 1}
        else {break}
    }
    return h
}