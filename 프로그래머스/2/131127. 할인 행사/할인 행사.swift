import Foundation

func solution(_ want:[String], _ number:[Int], _ discount:[String]) -> Int {
    
    var answer = 0
    var total = number.reduce(0,+)
    
    var standard: [String: Int] = [:]
    for i in 0..<want.count {
        standard[want[i]] = number[i]
    }
    
    for st in 0...discount.count-total {
        let arr = Array(discount[st..<st+total])
        var dict: [String: Int] = [:]
        for a in arr {
            dict[a, default:0] += 1
        }
        if dict == standard { answer += 1 }
    }
    
    return answer
}