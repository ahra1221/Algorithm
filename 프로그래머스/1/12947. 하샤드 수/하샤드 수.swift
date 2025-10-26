func solution(_ x:Int) -> Bool {
    let arr = String(x).map{ Int(String($0))! }
    let sum = arr.reduce(0,+)
    return x % sum == 0
}