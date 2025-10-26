func solution(_ s:String) -> Bool {
    if s.count == 4 || s.count == 6 {
        return s.allSatisfy { $0.isNumber }
    }
    return false

}