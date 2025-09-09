class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        partner = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in partner.values():
                st.append(i)
            else:
                if not st or partner[i] != st.pop():
                    return False
        return not st
        