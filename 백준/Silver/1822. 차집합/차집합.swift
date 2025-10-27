import Foundation

let n = readLine()!.split(separator: " ").map{Int($0)!}
let (a,b) = (n[0], n[1])
let aset = Set(readLine()!.split(separator: " ").map{Int($0)!})
let bset = Set(readLine()!.split(separator: " ").map{Int($0)!})
let ans = aset.subtracting(bset).sorted()
print(ans.count)
print(ans.map{String($0)}.joined(separator: " "))