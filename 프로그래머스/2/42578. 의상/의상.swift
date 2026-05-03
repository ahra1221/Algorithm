import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dict: [String:Int] = [:]
    for clothe in clothes {
        let type = clothe[1]
        dict[type, default:0] += 1
    }
    var answer = 1
    for val in dict.values {
        answer *= (val+1)
    }
    return answer-1
}