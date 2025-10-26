import Foundation

func solution(_ numbers:String) -> Int {
    var chars = Array(numbers)
    var used = Array(repeating: false, count: chars.count)
    var made = Set<Int>()        
    
    func dfs(_ cur: String) {
        if !cur.isEmpty {
            made.insert(Int(cur)!)
        }
        for i in 0..<chars.count {
             if !used[i] {
                used[i] = true
                dfs(cur + String(chars[i]))
                used[i] = false
            }
        }
    }
    
    dfs("")
    
    func isPrime(_ num: Int) -> Bool {
        if num<2 { return false}
        let r = Int(Double(num).squareRoot())
        if r < 2 { return true }
        for i in 2...r {
            if num % i == 0 { return false }
        }
        return true
    }
    
    return made.filter{isPrime($0)}.count
}