import Foundation

func solution(_ s:String) -> Int {
    let dict = [
        "zero":"0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    ]
    var answer = ""
    var tmp = ""
    for x in s {
        if x.isNumber {
            if !tmp.isEmpty {
                if let val = dict[tmp] {
                    answer.append(val)
                    tmp = ""
                }
            }
            answer.append(String(x))
        } else {
            if let val = dict[tmp] {
                answer.append(val)
                tmp = String(x)
            } else {
                tmp.append(x)
            }
        }
    }
    if !tmp.isEmpty { 
        if let val = dict[tmp] {
            answer.append(val)
        }
    }
    return Int(answer)!
}