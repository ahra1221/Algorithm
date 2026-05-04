import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var grid:[Int: [Int]] = [:] 
    for i in 0..<n {
        for j in i+1..<n {
            if computers[i][j] == 1 {
                grid[i+1, default:[]].append(j+1)
                grid[j+1, default:[]].append(i+1)
            }
        }
    }
    
    var visited = Array(repeating: false, count: n+1)
    
    func bfs(_ st: Int) {
        var q = [st]
        var head = 0
        visited[st] = true
        
        while head < q.count {
            let cur = q[head]
            head += 1
            
            if let nexts = grid[cur]{
                for nxt in nexts {
                    if !visited[nxt] {
                        q.append(nxt)
                        visited[nxt] = true
                    }
                }
            }
        }
    }
    
    var answer = 0
    
    for i in 1...n {
        if !visited[i] {
            bfs(i)
            answer += 1
        }
    }
    
    
    return answer
}