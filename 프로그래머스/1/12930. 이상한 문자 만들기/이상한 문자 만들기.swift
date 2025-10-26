func solution(_ s:String) -> String {
    let arr = s.split(separator: " ", omittingEmptySubsequences: false).map{String($0)}
    var ans: [String] = []
    for word in arr {
        var tmp = ""
        for (idx, ch) in word.enumerated() {
            let c = String(ch)
            tmp += idx % 2 == 0 ? c.uppercased() : c.lowercased()
        }
        ans.append(tmp)
    }
    return ans.joined(separator: " ")
}