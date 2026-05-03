import Foundation

func solution(_ numbers:[Int]) -> String {
    var stringNum = numbers.map {String($0)}
    stringNum.sort {
        return $0 + $1 > $1 + $0
    }
    let answer = stringNum.joined()
    return answer.first == "0" ? "0" : answer
}