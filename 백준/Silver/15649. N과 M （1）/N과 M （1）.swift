import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
let (n,m) = (input[0], input[1])

var arr: [Int] = []
var used: [Bool] = Array(repeating: false, count: n+1)

func backtracking(_ depth: Int) {
    if depth == m {
        print(arr.map{String($0)}.joined(separator: " "))
        return
    }

    for i in 1...n {
        if used[i] { continue}
        used[i] = true
        arr.append(i)
        backtracking(depth+1)
        arr.removeLast()
        used[i] = false
    }
}

backtracking(0)