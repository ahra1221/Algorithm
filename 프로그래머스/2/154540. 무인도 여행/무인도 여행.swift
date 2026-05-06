import Foundation

func solution(_ maps:[String]) -> [Int] {
    
    var grid = maps.map { Array($0) }
    let n = grid.count
    let m = grid[0].count
    
    var visited = Array(repeating: Array(repeating: false, count: m), count: n)
    let dirx = [1,-1,0,0]
    let diry = [0,0,1,-1]
    
    func bfs(_ i: Int, _ j: Int) -> Int {
        var q = [(i,j)]
        var head = 0
        visited[i][j] = true
        var total = Int(String(grid[i][j]))!
        
        while head < q.count {
            let cur = q[head]
            head += 1
            let x = cur.0
            let y = cur.1
            
            for d in 0..<4 {
                let nx = x + dirx[d]
                let ny = y + diry[d]
                if 0<=nx && nx<n && 0<=ny && ny<m && !visited[nx][ny] && grid[nx][ny] != "X" {
                    q.append((nx,ny))
                    visited[nx][ny] = true
                    total += Int(String(grid[nx][ny]))!
                }
            }
        }
        
        return total
    } 
    
    var answer = [Int]()
    for i in 0..<n {
        for j in 0..<m {
            if grid[i][j] != "X" && !visited[i][j] {
                answer.append(bfs(i,j))
            }
        }
    }
    
    if answer.isEmpty {
        answer = [-1]
    }
    
    return answer.sorted()
}