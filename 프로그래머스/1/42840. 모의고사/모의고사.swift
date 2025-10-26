import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let people = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    var high = 0
    var ans: [Int] = []
    for (idx,p) in people.enumerated() {
        var score = 0
        for i in 0..<answers.count {
            if answers[i] == p[i % p.count] {
                score += 1
            }
        }
        if score > high {
            high = score
            ans = [idx+1]
        } else if score == high {
            ans.append(idx+1)
        }
    }
    
    return ans
}