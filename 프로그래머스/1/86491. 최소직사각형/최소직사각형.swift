import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var wcan: [Int] = []
    var hcan: [Int] = []
    for size in sizes {
        let (w,h) = (size[0],size[1])
        wcan.append(max(w,h))
        hcan.append(min(w,h))
    }
    return wcan.max()! * hcan.max()!
}