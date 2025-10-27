import Foundation

func solution(_ sequence:[Int], _ k:Int) -> [Int] {
    var st = 0
    var en = 0
    var ans = [0, sequence.count - 1]
    var sum = sequence[st]
    while en < sequence.count {
        if sum == k {
            if en-st < ans[1]-ans[0] {
                ans = [st, en]
            }
            sum -= sequence[st]
            st += 1
        } else if sum < k {
            en += 1
            if en == sequence.count { break }
            sum += sequence[en]
        } else {
            sum -= sequence[st]
            st += 1
        }
    }
    return ans
}