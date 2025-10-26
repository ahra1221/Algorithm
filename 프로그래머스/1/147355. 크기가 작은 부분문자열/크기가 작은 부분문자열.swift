import Foundation

func solution(_ t:String, _ p:String) -> Int {
    let size = p.count
    let chars = Array(t)
    var sub: [String] = []
    for i in 0...(chars.count - size) {
        let tmp = String(chars[i...i+size-1])
        sub.append(tmp)
    }
    
    var ans = 0
    for s in sub {
        let num = Int(s)!
        if num <= Int(p)! {
            ans += 1
        }
    }
    return ans
}