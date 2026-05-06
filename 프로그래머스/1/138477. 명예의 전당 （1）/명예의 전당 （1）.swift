import Foundation

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    
    var answer = [Int]()
    
    var rank = [Int]()
    for s in score {
        if rank.count < k {
            rank.append(s)
            answer.append(rank.min()!)
            continue
        }
        
        var minVal = rank.min()!
        if s > minVal {
            if let idx = rank.firstIndex(of: minVal) {
                rank.remove(at: idx)
            }
            rank.append(s)
            minVal = rank.min()!
        }
        answer.append(minVal)
    }
    return answer
}