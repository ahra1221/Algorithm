import Foundation

func solution(_ s:String) -> Bool
{
    var st: [String] = []
    
    for i in Array(s) {
        if i == "(" {
            st.append(String(i))
        } else {
            if st.isEmpty {
                return false
            } else {
                if st.last == "(" {
                    st.removeLast()
                }
            }
        }
    }

    return st.isEmpty ? true : false
}