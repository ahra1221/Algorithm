import Foundation

func solution(_ k:Int, _ tangerine:[Int]) -> Int {
    var dict: [Int:Int] = [:]
    for tan in tangerine {
        dict[tan, default:0] += 1
    }
    
    let sortedDict = dict.sorted {$0.value > $1.value}
    var need = k
    var answer = 0
    for s in sortedDict {
        if need <= 0 { break }
        
        let v = s.value
        need -= v
        answer += 1
    }
    return answer
}