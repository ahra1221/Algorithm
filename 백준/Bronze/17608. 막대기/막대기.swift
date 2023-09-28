import Foundation

let total = Int(readLine()!)! // 6
var i: Int = 0
var array : [Int] = []
var bar: Int = 0
var answer: Int = 1

while i < total {
    let x = Int(readLine()!)!
    array.append(x)
    i = i + 1
}

i = i - 1
bar = array[i]

while i > 0 {
    i = i - 1
    if (array[i] <= bar) {
        continue
    } else {
        answer = answer + 1
        bar = array[i]
    }
}

print(answer)