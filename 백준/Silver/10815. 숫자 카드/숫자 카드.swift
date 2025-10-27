import Foundation

let n = Int(readLine()!)!
let sangeun = Set(readLine()!.split(separator: " ").map{Int($0)!})
let m = Int(readLine()!)!
let cand = readLine()!.split(separator: " ").map{Int($0)!}

var ans: [Int] = []

for c in cand {
    if sangeun.contains(c) {
        ans.append(1)
    } else {
        ans.append(0)
    }
}
print(ans.map{String($0)}.joined(separator: " "))