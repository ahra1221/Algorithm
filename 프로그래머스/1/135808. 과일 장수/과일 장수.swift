import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    let box = score.count / m
    var sc = score.sorted(by:>)
    var total = 0
    for i in stride(from:0, to: box * m, by: m) {
        let sub = sc[i..<i+m]
        total += sub.min()!
    }
    return total * m
}