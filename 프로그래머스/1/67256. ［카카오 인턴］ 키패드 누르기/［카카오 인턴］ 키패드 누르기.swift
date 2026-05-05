import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    
    let keypad = [
        1: (0,0), 2:(0,1), 3:(0,2),
        4: (1,0), 5:(1,1), 6:(1,2),
        7: (2,0), 8:(2,1), 9:(2,2),
        0: (3,1)
    ]
    
    var lefthand = (3,0)
    var righthand = (3,2)
    var answer = ""
    
    for num in numbers {
        let (nx, ny) = keypad[num]!
        var isLeft = true
        if ny == 2 { // 오른손
            isLeft = false
        } else if ny == 1 { // 거리비교 
            let leftDiff = abs(lefthand.0-nx) + abs(lefthand.1-ny)
            let rightDiff = abs(righthand.0-nx) + abs(righthand.1-ny)
            
            if leftDiff == rightDiff && hand == "right" {
                isLeft = false
            } else {
                if leftDiff > rightDiff {
                    isLeft = false
                } 
            }
        }
        
        if isLeft {
            lefthand = (nx,ny)
            answer.append("L")
        } else {
            righthand = (nx,ny)
            answer.append("R")
        }
    }
    
    return answer
}