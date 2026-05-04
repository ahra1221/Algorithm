import Foundation

func solution(_ rows:Int, _ columns:Int, _ queries:[[Int]]) -> [Int] {
    
    var answer = [Int]()
    
    var grid:[[Int]] = Array(repeating:Array(repeating:0, count: columns), count: rows)
    var num = 1
    for r in 0..<rows {
        for c in 0..<columns {
            grid[r][c] = num
            num += 1
        }
    }
    
    let dirx = [0,1,0,-1]
    let diry = [1,0,-1,0]
    
    for q in queries {
        let (x1, y1, x2, y2) = (q[0]-1, q[1]-1, q[2]-1, q[3]-1)
        
        var x = x1
        var y = y1
        var d = 0
        var prev = grid[x][y]
        var minValue = prev
        
        while true {
            minValue = min(minValue, prev)
            var nx = x + dirx[d]
            var ny = y + diry[d]
            
            if nx<x1 || nx>x2 || ny<y1 || ny>y2 {
                d += 1
                if d == 4 {break}
                nx = x + dirx[d]
                ny = y + diry[d]
            }
            let now = grid[nx][ny]
            grid[nx][ny] = prev
            prev = now
            
            x = nx
            y = ny
        }
        answer.append(minValue)
    }
    return answer
}