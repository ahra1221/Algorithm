import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let p1 = [1, 2, 3, 4, 5]
    let p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    let p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    var cnt = [0,0,0]
    
    for (idx,ans) in answers.enumerated() {
        if p1[idx%p1.count] == ans { cnt[0] += 1 }
        if p2[idx%p2.count] == ans { cnt[1] += 1 }
        if p3[idx%p3.count] == ans { cnt[2] += 1 }
    }
    
    let max = cnt.max()
    var answer = [Int]()
    for (idx,c) in cnt.enumerated() {
        if c == max { answer.append(idx+1)}
    }
    
    return answer.sorted()
}