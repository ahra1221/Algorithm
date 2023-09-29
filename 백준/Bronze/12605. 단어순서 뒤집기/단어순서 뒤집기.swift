let total = Int(readLine()!)!
var array : [String] = []
var num: Int = 0

for _ in 1...total {
    array.append(readLine()!)
}

for i in array {
    num += 1
    var string = i.split(separator: " ")
    var reverseString = ""
    string.reverse()
    for j in 0..<string.count {
        reverseString += string[j] + " "
    }
    print("Case #\(num): \(reverseString)")
}