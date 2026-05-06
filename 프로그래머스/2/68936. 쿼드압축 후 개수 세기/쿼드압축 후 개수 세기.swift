import Foundation

func solution(_ arr:[[Int]]) -> [Int] {
    
    var zero = 0
    var one = 0
    
    func canZip(_ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) -> Int {
        let first = arr[x1][y1]
        for x in x1...x2 {
            for y in y1...y2 {
                if arr[x][y] != first {
                    return -1
                }
            }
        }
        return first
    }
    
    func dfs(_ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) {
        let result = canZip(x1, y1, x2, y2)
        
        if result >= 0 {
            if result == 0 {
                zero += 1
            } else {
                one += 1
            }
            return
        }
        
        let half = (x2-x1+1)/2
        
        dfs(x1, y1, x1 + half - 1, y1 + half - 1)
        dfs(x1 + half, y1, x2, y1 + half - 1)
        dfs(x1, y1 + half, x1 + half - 1, y2)
        dfs(x1 + half, y1 + half, x2, y2)
    }
    
    dfs(0,0,arr.count-1,arr.count-1)
    
    return [zero,one]
}