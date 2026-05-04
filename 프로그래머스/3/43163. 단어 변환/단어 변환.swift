import Foundation

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {
    
    var answer = 0
    
    func isOneDiff(_ s1: String, _ s2: String) -> Bool {
        var diff = 0
        
        let arr1 = Array(s1)
        let arr2 = Array(s2)
        
        for i in 0..<arr1.count {
            if arr1[i] != arr2[i] { diff += 1 }
        }
        
        return diff == 1
    }
    
    var visited = Array(repeating: false, count: words.count)
    
    func dfs(_ cur: String, _ cnt: Int) {
        if cur == target {
            answer = cnt
            return
        }
        
        for (idx, word) in words.enumerated() {
            if !visited[idx] && isOneDiff(cur, word) {
                visited[idx] = true
                dfs(word, cnt+1)
                visited[idx] = false
            }
        }
    }
    
    dfs(begin, 0)
    
    return answer
}