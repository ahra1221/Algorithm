import Foundation

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    var time = 0
    
    var waitHead = 0
    var bridgeHead = 0
    var bridge = [(Int,Int)]() // weight time
    var total = 0
    while(waitHead < truck_weights.count || bridgeHead  < bridge.count) {
        // 현재 시간 계산해서 내보내기
        while bridgeHead < bridge.count {
            let (w,t) = bridge[bridgeHead]
            if time - t >= bridge_length {
                total -= w
                bridgeHead += 1
            } else {
                break
            }
        }
        
        // 들어갈수있는 트럭 넣기
        if(waitHead < truck_weights.count) {
            let nxt = truck_weights[waitHead]
            if (total + nxt <= weight) { // 다음꺼 들어갈수있음
                bridge.append((nxt, time))
                waitHead += 1
                total += nxt
            }
        }
        
        time += 1
    }
    
    return time
}