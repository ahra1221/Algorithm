import Foundation

func solution(_ maps:[String]) -> Int {
    
    var maps = maps.map {Array($0)}
    let r = maps.count
    let c = maps[0].count
    
    var sx = 0, sy = 0
    var lx = 0, ly = 0
    for i in 0..<r {
        for j in 0..<c {
            if maps[i][j] == "S" {
                sx = i
                sy = j
            }
            else if maps[i][j] == "L" {
                lx = i
                ly = j
            }
        }
    }
    
    let dirx = [-1,1,0,0]
    let diry = [0,0,-1,1]
    
    func bfs(_ sx: Int, _ sy: Int, _ end: Character) -> Int {
        
        var q = [(sx,sy,0)]
        var head = 0
        var visited = Array(repeating: Array(repeating: false, count: c), count: r)
        visited[sx][sy] = true
    
        while head < q.count {
            let (x,y,dist) = q[head]
            head += 1
            if maps[x][y] == end { 
                return dist
            }

            for i in 0..<4 {
                let nx = x+dirx[i]
                let ny = y+diry[i]
                if(0<=nx && nx<r && 0<=ny && ny<c && maps[nx][ny] != "X" && !visited[nx][ny]) {
                    q.append((nx,ny,dist+1))
                    visited[nx][ny] = true
                }
            }
        }
        return -1
    }
    
    var answer = 0
    let toL = bfs(sx,sy,"L")
    let toE = bfs(lx,ly,"E")
    

    if toL == -1 || toE == -1 {
        return -1
    }

    return toL + toE
}