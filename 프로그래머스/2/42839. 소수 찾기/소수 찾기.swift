import Foundation

func solution(_ numbers:String) -> Int {
    
    let number = Array(numbers)
    var answer = 0
    var numSet: Set<Int> = []
    
    func isPrime(_ num: Int) -> Bool {
        if num < 2 {return false}
        if num == 2 {return true}
        
        for i in 2..<num {
            if i*i > num {break}
            if num%i==0 {return false}
        }
        return true
    }
    
    func backtracking(_ cur: [Int]) {
        if !cur.isEmpty {
            var target = ""
            for c in cur {
                target.append(number[c])
            }
            if isPrime(Int(target)!) && !numSet.contains(Int(target)!) { 
                answer += 1 
                numSet.insert(Int(target)!)
            }
        }
        
        for i in 0..<numbers.count {
            if(!cur.contains(i)) {
                var nxt = cur
                nxt.append(i)
                backtracking(nxt)
            }
        }
    }
    
    backtracking([])
    
    return answer
}