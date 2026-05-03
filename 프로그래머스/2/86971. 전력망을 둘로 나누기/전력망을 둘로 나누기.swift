import Foundation

func solution(_ n:Int, _ wires:[[Int]]) -> Int {
    
    var dict:[Int: [Int]] = [:]
    for wire in wires {
        dict[wire[0], default: []].append(wire[1])
        dict[wire[1], default: []].append(wire[0])
    }
    
    func bfs(_ st: Int, _ cut: Int) -> Int {
        var q = [st]
        var head = 0
        var visited = Array(repeating: false, count: wires.count+2)
        visited[st] = true
        var count = 1
        
        while(head < q.count) {
            let cur = q[head]
            head += 1
            
            if let arr = dict[cur] {
                for nxt in arr {
                    if (cur == st && nxt == cut) || (cur==cut && nxt==st) {
                        continue
                    }
                    
                    if(!visited[nxt]) {
                        q.append(nxt)
                        visited[nxt] = true
                        count += 1
                    }
                }   
            }
        }
        return count
    }
    
    var answer = wires.count+2
    for (k,v) in dict {
        for x in v {
            let diff = abs(bfs(k,x) - bfs(x,k))
            answer = min(answer, diff)
        }
    }
    
    return answer
}