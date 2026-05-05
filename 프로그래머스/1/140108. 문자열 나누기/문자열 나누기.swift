import Foundation

func solution(_ s:String) -> Int {
    var answer = 0
    var s = Array(s)
    while true {
        let x = s[0]
        var xcount = 1, notx = 0
        var idx = 1
        while (idx < s.count && xcount != notx) {
            if s[idx] == x { xcount += 1 }
            else { notx += 1 }
            idx += 1
        }
        answer += 1
        if(idx < s.count) {
            s = Array(s[idx..<s.count])
        } else {
            break
        }
    }
    
    return answer
}