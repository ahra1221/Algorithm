import Foundation

func solution(_ s:String) -> Bool
{
    var ans:Bool = false
    var st = [Character]()
    for c in s {
        if c == "(" { st.append(c) }
        else {
            if !st.isEmpty && st.last! == "(" {
                st.removeLast();
            } else {
                st.append(c)
            }
        }
    }

    return st.isEmpty
}