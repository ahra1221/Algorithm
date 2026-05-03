import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var answer = [Int]()
    
    var total: [String: Int] = [:] // 장르별 총합
    var detail: [String: [(Int,Int)]] = [:] // plays, index
    
    for (idx, genre) in genres.enumerated() {
        total[genre, default:0] += plays[idx]
        detail[genre, default:[]].append((plays[idx],idx))
    }
    let sortedTotal = total.sorted {$0.value > $1.value}
    for x in sortedTotal {
        if var play = detail[x.key] {
            play.sort {
                if ($0.0 == $1.0) { return $0.1 < $1.1}
                return $0.0 > $1.0
            }
            if play.count >= 2 { play = Array(play[0..<2]) } 
            for (_,i) in play {
                answer.append(i)
            }
        }
    }
    
    return answer
}