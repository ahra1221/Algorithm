func solution(_ s:String) -> String {
    
    var answer = ""
    var index = 0
    for (idx, x) in s.enumerated() {
        if x == " " {
            answer.append(x)
            index = 0
        } else {
            if index == 0 {
                answer.append(x.uppercased())
            } else {
                answer.append(x.lowercased())
            }
            index += 1
        }
    }
    
    return answer
}