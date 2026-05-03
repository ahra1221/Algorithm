import Foundation

func solution(_ park:[String], _ routes:[String]) -> [Int] {
    let r = park.count
    let c = park[0].count
    var x = 0, y = 0
    
    var board = park.map {Array($0)}
    var dirs = [
        "E": (0,1), "W": (0,-1), "N": (-1,0), "S": (1,0)
    ]
    
    for i in 0..<r {
        for j in 0..<c {
            if board[i][j] == "S" {
                x = i
                y = j
                break
            }
        }
    }
    
    for route in routes {
        let tmp = Array(route.split(separator: " "))
        let dir = String(tmp[0])
        let dist = Int(tmp[1])!
        
        var nx = x
        var ny = y
        var canMove = true
        
        for _ in 0..<dist {
            nx += dirs[dir]!.0
            ny += dirs[dir]!.1
            
            if 0>nx || nx>=r || 0>ny || ny>=c {
                canMove = false
                break
            }
            
            if(board[nx][ny] == "X") {
                canMove = false
                break
            }
        }
        if canMove {
            x = nx
            y = ny
        }
    }
    
    return [x,y]
}