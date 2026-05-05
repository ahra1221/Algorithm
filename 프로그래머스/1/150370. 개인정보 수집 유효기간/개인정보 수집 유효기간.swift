import Foundation

func solution(_ today:String, _ terms:[String], _ privacies:[String]) -> [Int] {
    
    func toDays(_ date: String) -> Int {
        let d = date.split(separator: ".").map {Int($0)!}
        return d[0] * 28 * 12 + d[1] * 28 + d[2]
    }
    
    let todayDays = toDays(today)
    
    var termDict: [String: Int] = [:]
    for term in terms {
        let tmp = Array(term.split(separator: " ").map{String($0)})
        termDict[tmp[0]] = Int(tmp[1])!
    }
    
    var answer = [Int]()
    
    for i in 0..<privacies.count {
        let p = privacies[i].split(separator: " ")
        let start = String(p[0])
        let type = String(p[1])
        
        let expire = toDays(start) + termDict[type]! * 28
        
        if expire <= todayDays {
            answer.append(i+1)
        }
    }
    
    return answer
}