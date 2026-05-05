import Foundation

func solution(_ places:[[String]]) -> [Int] {
    
    let n = 5
    var result = [Int]()
    
    func check(
        _ sx: Int, 
        _ sy: Int, 
        _ grid: [[Character]]
    ) -> Bool {
        let oneDir = [(1,0),(-1,0),(0,1),(0,-1)]
        let twoDir = [(0,2),(2,0)]
        let crossDir = [(1,1),(1,-1)]
        
        for d in oneDir {
            let nx = sx+d.0, ny = sy+d.1
            if(0>nx || nx>=n || 0>ny || ny>=n) { continue }
            if grid[nx][ny] == "P" { return false }
        }
        
        for d in twoDir {
            let nx = sx+d.0, ny = sy+d.1
            if(0>nx || nx>=n || 0>ny || ny>=n) { continue }
            if grid[nx][ny] == "P" && grid[sx+d.0/2][sy+d.1/2] != "X" { 
                return false
            }
        }
        
        for d in crossDir {
            let nx = sx+d.0, ny = sy+d.1
            if(0>nx || nx>=n || 0>ny || ny>=n) { continue }
            if grid[nx][ny] == "P" { 
                if grid[sx][ny] != "X" || grid[nx][sy] != "X" {
                    return false
                }
            }
        }
        
        return true
    }
    
    for p in places {
        let place = p.map {Array($0)}
        var ans = true
        for i in 0..<n {
            for j in 0..<n {
                if place[i][j] == "P" {
                    if !check(i,j,place) {
                        ans = false
                        break
                    }
                }
            }
            if !ans { break }
        }
        result.append(ans ? 1 : 0)
    }

    
    
    return result
}