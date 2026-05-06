import Foundation

func solution(_ rows:Int, _ columns:Int, _ queries:[[Int]]) -> [Int] {
    
    var answer = [Int]()
    
    var grid = Array(repeating: Array(repeating: 0, count: columns), count: rows)
    var num = 1
    for i in 0..<rows {
        for j in 0..<columns {
            grid[i][j] = num
            num += 1
        }
    }
    
    let dirx = [0,1,0,-1]
    let diry = [1,0,-1,0]
    
    
    for query in queries {        
        let sx = query[0]-1
        let sy = query[1]-1
        let ex = query[2]-1
        let ey = query[3]-1
        
        var x = sx
        var y = sy
        
        var prev = grid[sx][sy]
        var d = 0
        var minVal = prev
        
        while true {
            minVal = min(minVal, prev)
            var nx = x + dirx[d]
            var ny = y + diry[d]
            if nx<sx || nx>ex || ny<sy || ny>ey {
                d += 1
                if d == 4 { break }
                nx = x + dirx[d]
                ny = y + diry[d]
            }
            let now = grid[nx][ny]
            grid[nx][ny] = prev
            prev = now
            
            x = nx
            y = ny
        }
        answer.append(minVal)
    }
    
    return answer
}