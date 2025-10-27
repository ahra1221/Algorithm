import Foundation

let n = Int(readLine()!)!
let m = Int(readLine()!)!
var dict = [Int: [Int]]()
for _ in 0..<m {
    let l = readLine()!.split(separator: " ").map{Int($0)!}
    dict[l[0], default: []].append(l[1])
    dict[l[1], default: []].append(l[0])
}

var visited = Array(repeating: false, count: n+1)

func bfs(_ node: Int) -> Int {
    var queue = [node]
    visited[node] = true
    var idx = 0
    var count = 0
    while idx < queue.count {
        let cur = queue[idx]
        count += 1
        idx += 1
        for n in dict[cur, default: []] {
            if !visited[n] {
                visited[n] = true
                queue.append(n)
            }
        }
    }
    return count
}

print(bfs(1)-1)