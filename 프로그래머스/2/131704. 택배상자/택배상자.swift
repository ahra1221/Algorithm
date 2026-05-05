import Foundation

func solution(_ order:[Int]) -> Int {
    
    var subBelt = [Int]()
    var box = 1
    var answer = 0
    
    for ord in order {
        while box <= ord {
            subBelt.append(box)
            box += 1
        }
        
        if subBelt.last == ord {
            subBelt.removeLast()
            answer += 1
        } else {
            break
        }
    }
    
    return answer
}