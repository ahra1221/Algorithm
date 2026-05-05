import Foundation

func solution(_ n:Int) -> Int {
    var isPrime = Array(repeating: true, count: n+1)
    isPrime[0] = false
    isPrime[1] = false
    
    for i in 2...n {
        if i*i > n { break }
        if isPrime[i] {
            var j = i * i
            while (j <= n) {
                isPrime[j] = false
                j += i
            }
        }
    }
    return isPrime.filter{ $0 }.count
}