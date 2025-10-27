import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
let (n,m) = (input[0], input[1])
let dir = [
    (1,0), (-1,0), (0,1),(0,-1)
]

var board = [[Int]]()
for _ in 0..<n {
    let row = readLine()!.map { Int(String($0))! }
    board.append(row)
}
var visited = Array(repeating: Array(repeating: false, count: m), count: n)
var cnt = Array(repeating: Array(repeating: 0, count: m), count: n)

func bfs(_ r: Int,_ c: Int) {
    var q = [(r,c)]
    visited[r][c] = true
    cnt[r][c] = 1
    var idx = 0
    while idx < q.count {
        let (nr, nc) = q[idx]
        idx += 1
        for (dx, dy) in dir {
            var sr = nr + dx
            var sc = nc + dy
            if sr >= 0 && sr < n && sc >= 0 && sc < m && board[sr][sc] == 1 && !visited[sr][sc] {
                q.append((sr,sc))
                visited[sr][sc] = true
                cnt[sr][sc] = cnt[nr][nc] + 1
            }
        }
    }
}

bfs(0,0)
print(cnt[n-1][m-1])