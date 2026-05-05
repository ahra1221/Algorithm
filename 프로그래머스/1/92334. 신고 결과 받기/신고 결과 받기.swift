import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    
    var answer = Array(repeating: 0, count: id_list.count)
    var indexDict: [String: Int] = [:]
    for i in 0..<id_list.count {
        indexDict[id_list[i]] = i
    }
    
    var reportDict: [String: Set<String>] = [:]
    for r in report {
        let arr = r.split(separator: " ").map { String($0) }
        reportDict[arr[1], default:[]].insert(arr[0])
    }
    
    let stopped = reportDict.filter {$0.value.count >= k }
    for stop in stopped.values {
        for s in stop {
            answer[indexDict[s]!] += 1
        }
    }
    
    return answer
}