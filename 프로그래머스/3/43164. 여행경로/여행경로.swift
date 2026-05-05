import Foundation

func solution(_ tickets:[[String]]) -> [String] {
    let tickets = tickets.sorted {
        if $0[0] == $1[0] {
            return $0[1] < $1[1]
        }
        return $0[0] < $1[0]
    }
    
    var dict: [String:[String]] = [:]
    for t in tickets {
        dict[t[0], default:[]].append(t[1])
    }
    
    var visited = Array(repeating: false, count: tickets.count)
    var answer = [String]()
    
    func dfs(_ st: String, _ route: [String]) -> Bool {
        if route.count == tickets.count + 1 {
            answer = route
            return true
        }
        
        for i in 0..<tickets.count {
            if !visited[i] && tickets[i][0] == st {
                visited[i] = true
                if dfs(tickets[i][1], route + [tickets[i][1]]) {
                    return true
                }
                visited[i] = false
            }
        }
        return false
    }
    _ = dfs("ICN", ["ICN"])
    return answer
}