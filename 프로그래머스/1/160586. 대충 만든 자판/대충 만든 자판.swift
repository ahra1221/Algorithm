import Foundation

func solution(_ keymap:[String], _ targets:[String]) -> [Int] {
    
    var answer = [Int]()
    
    var maps: [Character: Int] = [:]
    for key in keymap {
        let chars = Array(key)
        for (idx, c) in chars.enumerated() {
            if let val = maps[c] {
                maps[c] = min(val,idx+1) 
            } else {
                maps[c] = idx+1
            }
        }
    }
    
    for target in targets {
        let t = Array(target)
        var total = 0
        var canMap = true
        for x in t {
            if let cnt = maps[x] {
                total += cnt
            } else {
                canMap = false
                break
            }
        }
        answer.append(canMap ? total : -1)
    }
    
    return answer
}