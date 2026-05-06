import Foundation

func solution(_ t:String, _ p:String) -> Int {
    var answer = 0
    let n = p.count
    
    var ts = Array(t)
    for st in 0...t.count-n {
        let num = Array(ts[st..<st+n])
        let sub = Int(String(num))!
        if sub <= Int(p)! {
            answer += 1
        }
    }
    return answer
}