import Foundation

func checkRight(_ target: String) -> Bool { // 올바른 괄호
    var st = [Character]()
    for t in target {
        if t == "(" { st.append(t) }
        else {
            if(!st.isEmpty && st.last! == "(") {
                st.removeLast()
            } else {
                st.append(t)
            }
        }
    }
    return st.isEmpty
}

func findBalance(_ target: String) -> (String,String) { // 균형잡힌 괄호 문자열로 분리
    var u = "", v = ""
    let tmp = Array(target)
    var openCnt = 0, closeCnt = 0
    for (idx,t) in target.enumerated() {
        if t == "(" { openCnt += 1 }
        else { closeCnt += 1 }
        
        if openCnt == closeCnt {
            u = String(tmp[0...idx])
            v = String(tmp[idx+1..<target.count])
            break
        }
    }
    return (u,v)
}

func reverseDir(_ target: String) -> String {
    var rev = ""
    for t in target {
        if t == "(" { rev += ")"}
        else { rev += "("}
    }
    return rev
}

func solution(_ p:String) -> String {
    if p.isEmpty {return ""}
    if checkRight(p) {return p}
    
    var (u, v) = findBalance(p)
    if checkRight(u) {
        return u + solution(v)
    } else {
        let answer = "(" + solution(v) + ")"
        let sub = reverseDir(String(Array(u)[1..<u.count-1]))
        return answer + sub
    }
    return ""
}