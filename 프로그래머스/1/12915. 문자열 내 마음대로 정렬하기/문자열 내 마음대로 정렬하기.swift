func solution(_ strings:[String], _ n:Int) -> [String] {
    return strings.sorted {
        let c1 = $0[$0.index($0.startIndex, offsetBy: n)]
        let c2 = $1[$1.index($1.startIndex, offsetBy: n)]
        if c1 == c2 {
            return $0 < $1
        } else {
            return c1 < c2
        }
    }
}