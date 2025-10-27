import Foundation

let n = Int(readLine()!)!
var words: [String] = []

for _ in 0..<n {
    words.append(readLine()!)
}

var ans = 0

for w in words {
    var dic = [String: Int]()
    let arr = Array(String(w))
    var isValid = true

    for (idx, k) in arr.enumerated() {
        let k = String(k)
        if let val = dic[k] {
            if (idx - val) == 1 {
                dic[k] = idx
            } else {
                isValid = false
                break
            }
        } else {
            dic[k] = idx
        }
    }
    if isValid {
        ans += 1
    }
}
print(ans)