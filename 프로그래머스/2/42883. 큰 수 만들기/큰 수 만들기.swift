import Foundation

func solution(_ number:String, _ k:Int) -> String {
    var st = [Character]()
    var k = k
    
    for num in number {
        while k > 0 && !st.isEmpty && st.last! < num {
            st.removeLast()
            k -= 1
        }
        st.append(num)
    }
    
    if k > 0 {
        st.removeLast(k)
    }
    
    return String(st)
}