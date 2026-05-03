import Foundation

func solution(_ s:String) -> Int {
    
    let arr = Array(s)
    let n = arr.count
    var answer = n
    
    if n == 1 { return 1 }
    
    for step in 1...s.count/2 {
        var prev = ""
        var count = 1
        var zip = ""
        for i in stride(from: 0, to: s.count-step+1, by: step) {
            let sub = String(arr[i..<i+step])
            if prev == sub {
                count += 1
            } else {
                if !prev.isEmpty {
                    if count > 1 { zip += String(count) }
                    zip += prev
                } 
                prev = sub
                count = 1
            }
        }
        if count > 1 { zip += String(count) }
        zip += prev
        
        answer = min(answer, zip.count + s.count % step)
    }
    return answer
}