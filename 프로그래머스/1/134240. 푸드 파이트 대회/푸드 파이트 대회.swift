import Foundation

func solution(_ food:[Int]) -> String {
    var answer = ""
    for i in 1..<food.count {
        answer += String(repeating: String(i), count: food[i] / 2)
    }
    let rev = String(answer.reversed())
    return answer + "0" + rev
}