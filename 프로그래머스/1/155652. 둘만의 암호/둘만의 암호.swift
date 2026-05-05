import Foundation

func solution(_ s:String, _ skip:String, _ index:Int) -> String {
    
    var answer = ""
    let skipSet = Set(Array(skip).map{Int($0.asciiValue!)})
    
    for x in s {
        var now = Int(x.asciiValue!)
        var idx = 0
        
        while (idx < index) {
            now += 1
            
            if now > 122 { now = 97 }
            
            if !skipSet.contains(now) { 
                idx += 1
            }
        }
    	answer.append(Character(UnicodeScalar(now)!))   
    }
    return answer
}