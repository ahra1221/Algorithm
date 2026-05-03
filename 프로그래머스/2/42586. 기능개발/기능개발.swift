import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var answer = [Int]()
    var st = [Int]()
    for i in 0..<progresses.count {
        let need = (100 - progresses[i] + speeds[i] - 1) / speeds[i]
        if !st.isEmpty && st[0] < need {
            answer.append(st.count)
            st.removeAll()
        } 
        st.append(need)
    }
    if !st.isEmpty {answer.append(st.count)}
    return answer
}