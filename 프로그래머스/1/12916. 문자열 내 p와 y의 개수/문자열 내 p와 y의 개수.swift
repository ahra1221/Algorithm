import Foundation

func solution(_ s:String) -> Bool
{
    var ans:Bool = false
    
    var pcnt = 0, ycnt = 0;
    for c in s.lowercased() {
        if c == "p" {pcnt += 1}
        else if c == "y" {ycnt += 1}
    }
    
    if (pcnt == 0 && ycnt == 0) {return true}
    
    return pcnt == ycnt;
}