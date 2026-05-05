import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    
    var answer = 0
    let n = board.count
    var board = board
    
    var st = [Int]()
    for move in moves {
        var r = 0
        while r < n && board[r][move-1] == 0 {
            r += 1
        }
        if r == n { continue }
        
        let toy = board[r][move-1]
        if !st.isEmpty && st.last! == toy {
            st.removeLast()
            answer += 2
        } else {
            st.append(toy)
        }
        board[r][move-1] = 0
    }
    return answer
}