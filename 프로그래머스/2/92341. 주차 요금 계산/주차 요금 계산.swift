import Foundation

func solution(_ fees:[Int], _ records:[String]) -> [Int] {
    
    func calTime(_ st: String, _ en: String) -> Int {
        let start = Array(st.split(separator: ":").map{Int($0)!})
        let end = Array(en.split(separator: ":").map{Int($0)!})
        return 60 * (end[0] - start[0]) + (end[1] - start[1])
    }
    
    func calFee(_ during: Int) -> Int {
        var fee = fees[1]
        if during > fees[0] {
            let exceed = (during - fees[0] + fees[2] - 1)  / fees[2]
            fee += exceed * fees[3]
        }
        return fee
    }
    
    var inTime: [String: String] = [:]
    var total: [String: Int] = [:]
    for record in records {
        let arr = Array(record.split(separator: " ").map{String($0)})
        if arr[2] == "IN" {
            inTime[arr[1]] = arr[0]
        } else if arr[2] == "OUT" {
            let intime = inTime[arr[1]]!
            inTime[arr[1]] = nil
            let during = calTime(intime, arr[0])
            total[arr[1], default: 0] += during
        }
    }
    if inTime.count > 0 {
        for (number,t) in inTime {
            let during = calTime(t, "23:59")
            total[number, default: 0] += during
        }
    }
    
    var totalFee: [String: Int] = [:]
    for (n,t) in total {
        totalFee[n] = calFee(t)
    }
    let answer = totalFee.sorted{ $0.key < $1.key }.map{$0.value}
    return answer
}