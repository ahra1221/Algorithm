import Foundation

func solution(_ n:Int) -> Int {
    var result: [Int] = []
    if n == 0 {
        return 0
    }
    let limit = Int(sqrt(Double(n)))
    for i in 1...limit {
        if n % i == 0 {
            result.append(i)
            if i != n / i {
                result.append(n/i)
            }
        }
    }
    return result.reduce(0,+)
}