import Foundation

func solution(_ word:String) -> Int {
    
    var answer = 0
    var find = false
    
    func dfs(_ cur: String) {
        if find { return }
        if !cur.isEmpty {
            answer += 1
            if cur == word { 
                find = true
                return 
            }
        }
        if cur.count == 5 { return }
        
        for w in ["A", "E", "I", "O", "U"] {
            dfs(cur+w)
        }
    }
    
    dfs("")
    
    return answer
}