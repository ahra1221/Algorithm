import Foundation

func solution(_ board:[String]) -> Int {
    var grid = board.map{Array($0)}
    let r = grid.count, c = grid[0].count
    
    var sx = 0, sy = 0
    for i in 0..<r {
        for j in 0..<c {
            if grid[i][j] == "R" {
                sx = i
                sy = j
                break
            }
        }
    }
    
    var visited = Array(repeating: Array(repeating: false, count: c), count: r)
    let dirx = [-1,1,0,0]
    let diry = [0,0,-1,1]
    
    
    var q = [(sx,sy,0)]
    var head = 0
    visited[sx][sy] = true
    
    while(head < q.count) {
        let x = q[head].0, y = q[head].1, cnt = q[head].2
        head += 1
        if grid[x][y] == "G" { return cnt }
        
        for i in 0..<dirx.count {
            var nx = x, ny = y;
            while(0<=nx && nx<r && 0<=ny && ny<c && grid[nx][ny] != "D") {
                nx += dirx[i]
                ny += diry[i]
            }
            nx -= dirx[i]
            ny -= diry[i]
            if !visited[nx][ny] {
                q.append((nx,ny,cnt+1))
                visited[nx][ny] = true
            }
        }
    }

    
    return -1
}