import Foundation

func solution(_ skill:String, _ skill_trees:[String]) -> Int {
    
    var answer = 0
    
    var dict: [Character: Int] = [:]
    for (idx,s) in Array(skill).enumerated() {
        dict[s] = idx
    }
    
    for skills in skill_trees {
        var tmp = [Int]()
        for s in skills {
            if dict[s] != nil {
                tmp.append(dict[s]!)
            }
        }
        
        var vaild = true
        for i in 0..<tmp.count {
            if tmp[i] != i {
                vaild = false
                break
            }
        }
        
        if vaild {
            answer += 1
        }
    }
    return answer
}