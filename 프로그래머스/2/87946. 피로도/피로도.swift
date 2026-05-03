import Foundation

func solution(_ k:Int, _ dungeons:[[Int]]) -> Int {
    
    var answer = 0
    
    func backtracking(_ cur:[Int], _ now:Int) {
        answer = max(answer, cur.count)
        for (i, dungeon) in dungeons.enumerated() {
            let need = dungeons[i][0]
            if(!cur.contains(i) && need <= now) {
                var nxt = cur
                nxt.append(i)
                backtracking(nxt,now-dungeons[i][1])
            }
        }
    }
    
    backtracking([], k)
    
    return answer
}