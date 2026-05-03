import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var sortedsize = sizes.map {$0.sorted(by:>)}
    
    var width: Set<Int> = []
    var height: Set<Int> = []
    for size in sortedsize {
        width.insert(size[0])
        height.insert(size[1])
    }
    let answer = width.max()! * height.max()!
    return answer
}