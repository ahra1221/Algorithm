import Foundation

func solution(_ board:[String]) -> Int {
    var answer = 0
    
    var board = board.map { Array($0) }
     
    let n = board.count
    let m = board[0].count
    
    var start = (0,0)
    var end = (0,0)
    for i in 0..<n {
        for j in 0..<m {
            if board[i][j] == "R" {
                start = (i,j)
            } else if board[i][j] == "G" {
                end = (i,j)
            }
        }
    }
    
    let dirx = [1,-1,0,0]
    let diry = [0,0,1,-1]
    
    var q = [(start.0, start.1, 0)]
    var head = 0
    var visited = Array(repeating: Array(repeating: false, count: m), count: n)
    visited[start.0][start.1] = true
    
    while head < q.count {
        let cur = q[head]
        head += 1
        
        let x = cur.0
        let y = cur.1
        let c = cur.2
        
        if x==end.0 && y==end.1 {
            answer = c
        }
        
        for d in 0..<4 {
            var nx = x+dirx[d], ny = y+diry[d]
            while nx >= 0 && nx < n && ny >= 0 && ny < m && board[nx][ny] != "D" {
                nx += dirx[d]
                ny += diry[d]
            }
            nx -= dirx[d]
            ny -= diry[d]
            if !visited[nx][ny] {
                q.append((nx,ny,c+1))
                visited[nx][ny] = true
            }
        }
    }
    
    return answer > 0 ? answer : -1
}