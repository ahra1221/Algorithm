func solution(_ a:Int, _ b:Int) -> Int64 {
    var ans = Int64(0)
    let st = min(a,b)
    let en = max(a,b)
    if a != b {
        for i in st..<en+1 {
            ans += Int64(i)
        }
    }
    return a==b ? Int64(a) : ans
}