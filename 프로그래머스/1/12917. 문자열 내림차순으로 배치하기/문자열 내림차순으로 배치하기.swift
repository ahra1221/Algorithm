func solution(_ s:String) -> String {
    var lower = ""
    var upper = ""
    for c in s {
        if c.isLowercase { lower.append(c) }
        else { upper.append(c) }
    }
    var answer = ""
    answer += String(lower.sorted(by:>))
    answer += String(upper.sorted(by:>))
    return answer
}