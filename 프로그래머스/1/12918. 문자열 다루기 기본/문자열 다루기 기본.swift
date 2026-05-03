func solution(_ s:String) -> Bool {
    let cnt = s.count
    if((cnt==4 || cnt==6) && s.allSatisfy{$0.isNumber}) {
        return true
    }
    return false
}