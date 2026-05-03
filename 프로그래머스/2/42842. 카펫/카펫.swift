import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    for i in 1...Int(sqrt(Double(yellow))) {
        if yellow % i == 0 {
            let b = 2 * (i + yellow / i) + 4
            if b == brown { 
                return [i+2, yellow / i+2].sorted(by:>) 
            }
        }
    }
    return []
}