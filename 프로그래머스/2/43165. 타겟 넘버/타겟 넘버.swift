import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    
    var answer = 0
    
    func dfs(_ st: Int,_ total: Int) {
        if st == numbers.count {
            if total == target {
                answer += 1
            }
            return
        }
        
        dfs(st+1,total+numbers[st])
        dfs(st+1,total-numbers[st])
    }
    
    dfs(1,numbers[0])
    dfs(1,-numbers[0])
    
    return answer
}