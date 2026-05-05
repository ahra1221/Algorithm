import Foundation

func solution(_ number:Int, _ limit:Int, _ power:Int) -> Int {
    
    func find(_ num: Int) -> Int {
        var s: Set<Int> = []
        for i in 1...Int(sqrt(Double(num))) {
            if num % i == 0 {
                s.insert(i)
                s.insert(num / i)
            }
        }
        return s.count
    }
    
    var arr = Array(repeating: 1, count: number+1)
    arr[0] = 0
    for i in 1...number {
        let f = find(i)
        arr[i] = f > limit ? power : f
    }
    return arr.reduce(0,+)
}