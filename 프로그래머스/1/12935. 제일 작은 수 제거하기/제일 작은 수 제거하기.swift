func solution(_ arr:[Int]) -> [Int] {
    var arr = arr
    let minval = arr.min()!
    arr.remove(at: arr.firstIndex(of: minval)!)
    return arr.isEmpty ? [-1] : arr
}