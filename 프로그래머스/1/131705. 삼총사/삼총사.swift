import Foundation

func solution(_ number:[Int]) -> Int {
    
    var answer = 0
    
    func dfs(_ cur: Set<Int>, _ total: Int, _ st: Int) {
        if cur.count == 3 {
            if total == 0 {
                answer += 1   
            }
            return
        }
        
        for idx in st..<number.count {
            if !cur.contains(idx) {
                var nxt = cur
                nxt.insert(idx)
                dfs(nxt, total + number[idx], idx+1)
            }
        }
    }
    
    dfs([],0,0)
    
    return answer
}