class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        open_set = {"(", "{", "["}
        for i in s:
            if i in open_set:
                st.append(i)
            else:
                if not st:
                    return False
                o = st.pop()
                if i == ")" and o == "(":
                    continue
                elif i == "}" and o == "{":
                    continue
                elif i == "]" and o == "[":
                    continue
                else:
                    return False
        return not st
        