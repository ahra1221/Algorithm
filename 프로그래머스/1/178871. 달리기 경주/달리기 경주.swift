import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var player = players
    var rank: [String: Int] = [:]
    
    for (i, p) in player.enumerated() {
        rank[p] = i
    }
    
    for calling in callings {
        let cur = rank[calling]!
        let prevName = player[cur-1]
        
        player[cur-1] = calling
        player[cur] = prevName
        
        rank[calling] = cur - 1
        rank[prevName] = cur
    }
    
    return player
}