import Foundation

func solution(_ n:Int, _ times:[Int]) -> Int64 {
    var l = 1
    var r = times.max()! * n
    var ans = r
    
    while l <= r {
        let mid = (l + r) / 2
        var proceed = 0
        for t in times {
            proceed += mid / t
        }
        
        if proceed >= n {
            ans = mid
            r = mid - 1
        } else {
            l = mid + 1
        }
    }
    return Int64(ans)
}