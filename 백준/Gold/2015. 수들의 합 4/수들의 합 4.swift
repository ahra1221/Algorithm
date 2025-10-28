import Foundation

let nk = readLine()!.split(separator: " ").map { Int($0)! }
let (n, k) = (nk[0], nk[1])

let arr = readLine()!.split(separator: " ").map { Int($0)! }
var pref = 0 
var ans = 0
var freq = [0:1]

for x in arr {
    pref += x
    ans += freq[pref-k, default:0]
    freq[pref, default:0] += 1
}
print(ans)