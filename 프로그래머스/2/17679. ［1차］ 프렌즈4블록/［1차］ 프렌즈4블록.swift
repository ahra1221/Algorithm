func solution(_ m:Int, _ n:Int, _ board:[String]) -> Int {
    
    var boards = board.map {Array($0)}
    var answer = 0
    
    func findAndDel() -> Bool{
        var delete = [[(Int,Int)]]()
        
        let dirx = [1,0,1]
        let diry = [0,1,1]
        
        for i in 0..<m-1 {
            for j in 0..<n-1 {
                let cur = boards[i][j]
                if cur == "0" { continue }
                var candidate = [(i,j)]
                var isRect = true
                
                for d in 0..<3 {
                    let nx = i + dirx[d]
                    let ny = j + diry[d]
                    if boards[nx][ny] != cur {
                        isRect = false
                        break
                    }
                    candidate.append((nx,ny))
                }
                if isRect {
                    delete.append(candidate)
                }
            }
        }
        
        if delete.isEmpty {
            return false
        }
        
        for del in delete {
            for (x,y) in del {
                if boards[x][y] != "0" {
                    boards[x][y] = "0"
                    answer += 1
                }
            }
        }
        return true
    }
    
    func down() {
        for c in 0..<n {
            var write = m - 1
            
            for r in stride(from: m-1, through: 0, by: -1) {
                if boards[r][c] != "0" {
                    boards[write][c] = boards[r][c]
                    write -= 1
                }
            }
            
            while (write >= 0) {
                boards[write][c] = "0"
                write -= 1 
            }
        }
    }
    
    while(findAndDel()) {
        down()
    }
    
    return answer
}