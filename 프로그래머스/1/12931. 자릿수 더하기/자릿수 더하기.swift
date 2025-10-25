import Foundation

func solution(_ n:Int) -> Int
{
    let arr = String(n).compactMap { Int(String($0))! }
    let answer:Int = arr.reduce(0, +)
    return answer
}