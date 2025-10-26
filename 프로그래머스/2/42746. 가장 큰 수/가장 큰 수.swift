import Foundation

func solution(_ numbers:[Int]) -> String {
    let arr = numbers.map{String($0)}
    let sorted_arr = arr.sorted {$0 + $1 > $1 + $0}
    if sorted_arr[0] == "0" { return "0" }
    return sorted_arr.joined()
}