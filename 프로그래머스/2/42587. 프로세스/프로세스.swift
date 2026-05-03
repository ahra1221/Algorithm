import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    
    var q = [(Int,Int)]()
    for (idx, pri) in priorities.enumerated() {
        q.append((idx,pri))
    }
    
    var maxPri = priorities.max()!
    var head = 0
    var order = 1
    while head < q.count {
        let (curIndex, curPri) = q[head]
        head += 1
        
        if maxPri == curPri {
            if curIndex == location {
                return order
            } else {
                maxPri = Array(q[head..<q.count].map{$0.1}).max()!
                order += 1
            }
        } else {
            q.append((curIndex, curPri))
        }
    }
    
    return order
}