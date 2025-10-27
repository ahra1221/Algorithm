import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
let (n,m,v) = (input[0], input[1], input[2])
var dict = [Int: [Int]]()
for _ in 0..<m {
    let l = readLine()!.split(separator: " ").map{Int($0)!}
    dict[l[0], default: []].append(l[1])
    dict[l[1], default: []].append(l[0])
}

for i in 1...n {
    dict[i]?.sort()
}

var visited = Array(repeating: false, count: n+1)
func dfs(_ node: Int) {
    visited[node] = true
    print(node, terminator: " ")
    for n in dict[node, default: []] {
        if !visited[n] {
            dfs(n)
        }
    }
}

func bfs(_ node: Int) {
    var queue = [node]
    visited[node] = true
    var idx = 0
    while idx < queue.count {
        let cur = queue[idx]
        print(cur, terminator: " ")
        idx += 1
        for n in dict[cur, default: []] {
            if !visited[n] {
                visited[n] = true
                queue.append(n)
            }
        }
    }
}

dfs(v)
visited = Array(repeating: false, count: n+1)
print()
bfs(v)