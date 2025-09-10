class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def isNum(s):
            try:
                int(s)
                return True
            except:
                return False
        
        st = []
        for to in tokens:
            if isNum(to):
                st.append(to)
            else:
                num2 = st.pop()
                num1 = st.pop()
                st.append(trunc(eval(str(num1)+to+str(num2))))
        return int(st.pop())