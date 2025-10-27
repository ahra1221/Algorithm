import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let (n, m) = (input[0], input[1])

var s: Set<String> = []
for _ in 0..<n {
    s.insert(readLine()!)
}

var ans = 0
for _ in 0..<m {
    let testcase = readLine()!
    if s.contains(testcase) {
        ans += 1
    }
}

print(ans)