import Foundation

func solution(_ wallpaper:[String]) -> [Int] {
    
    var answer = [Int]()
    
    let wallpaper = wallpaper.map {Array($0)}
    let r = wallpaper.count
    let c = wallpaper[0].count
    
    var files = [(Int,Int)]()
    for i in 0..<r {
        for j in 0..<c {
            if wallpaper[i][j] == "#" {
                files.append((i,j))
            }
        }
    }
    
    let minx = files.map{$0.0}.min()!
    let miny = files.map{$0.1}.min()!
    let maxx = files.map{$0.0}.max()!
    let maxy = files.map{$0.1}.max()!
    
    answer = [minx,miny,maxx+1,maxy+1]
    
    return answer
}