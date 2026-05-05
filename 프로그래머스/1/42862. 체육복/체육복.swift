func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var lostSet = Set(lost)
    var reserveSet = Set(reserve)
    
    let both = lostSet.intersection(reserveSet)
    lostSet.subtract(both)
    reserveSet.subtract(both)
    
    var answer = n - lostSet.count
    
    for l in lostSet.sorted() {
        if reserveSet.contains(l-1) {
            answer += 1
            reserveSet.remove(l-1)
        } else if reserveSet.contains(l+1) {
            answer += 1
            reserveSet.remove(l+1)
        }
    }
    return answer
}