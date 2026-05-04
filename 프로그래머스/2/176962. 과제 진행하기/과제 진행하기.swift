import Foundation

func solution(_ plans:[[String]]) -> [String] {
    var plan = plans.sorted {$0[1] < $1[1]}
    
    func toMinute(_ time: String) -> Int {
        let t = Array(time.split(separator:":").map{Int($0)!})
        return 60 * t[0] + t[1]
    }
    
    var answer = [String]()
    var wait = [(String,Int)]()
    
    for (idx, p) in plan.enumerated() {
        let name = p[0]
        let start = toMinute(p[1])
        let play = Int(p[2])!
        
        if (idx != plan.count-1) {
            let nextStart = toMinute(plan[idx+1][1])
            var remain = nextStart - start
            
            if remain >= play {
                answer.append(name)
                remain -= play
            } else {
                wait.append((name,play-remain))
                remain = 0
            }
            
            while remain > 0 && !wait.isEmpty {
                let (n,t) = wait.removeLast()
                if remain < t { 
                    wait.append((n,t-remain))
                    remain = 0
                } else {
                    answer.append(n)
                    remain -= t
                }
            }
            
        } else {
            answer.append(name)
        }
    }
    
    while !wait.isEmpty {
        let (n,_) = wait.removeLast()
        answer.append(n)
    }
    
    return answer
}