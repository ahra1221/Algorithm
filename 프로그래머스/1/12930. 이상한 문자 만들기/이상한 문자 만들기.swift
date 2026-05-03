func solution(_ s:String) -> String {
    var answer = ""
    var idx = 0
    
    for c in s {
        if c == " " { 
            answer.append(c) 
            idx = 0
        } else {
            if(idx % 2 == 0) {answer += String(c).uppercased()}
            else {answer += String(c).lowercased()}
            idx += 1
        }
        
    }
    
    
    let arr = s.split(separator: " ")
    for a in arr {
        var str = ""
        for(idx, c) in a.enumerated() {
            if (idx % 2 == 0) {str.append(c.uppercased())}
            else {str.append(c.lowercased())}
        }
    }
    return answer
}