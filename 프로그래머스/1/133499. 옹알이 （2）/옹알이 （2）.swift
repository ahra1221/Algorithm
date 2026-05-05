import Foundation

func solution(_ babbling:[String]) -> Int {
    var answer = 0
    let word: Set<String> = ["aya", "ye", "woo", "ma"]
    
    func splitWord(_ target: String) -> Bool {
        print(target)
        let arr = Array(target)
        var w = ""
        var prev = ""
        for x in arr {
            w.append(x)
            if word.contains(w) {
                if prev != w {
                    prev = w
                    w = ""
                } else {
                    return false
                }
            }
        }
        if !w.isEmpty {
            if !word.contains(w) || prev == w {
                return false
            }
        }
        return true
    }
    
    for b in babbling {
        if word.contains(b) || splitWord(b){
            answer += 1
        } 
    }
    return answer
}