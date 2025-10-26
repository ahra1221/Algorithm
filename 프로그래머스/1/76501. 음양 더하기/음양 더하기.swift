import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var ans = 0
    for (num, sign) in zip(absolutes, signs) {
        if sign {
            ans += num
        } else {
            ans -= num
        }
    }
    return ans
}