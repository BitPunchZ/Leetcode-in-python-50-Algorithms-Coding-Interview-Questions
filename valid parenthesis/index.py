class Solution:
    def isEqual(self, c1, c2) -> bool:
        if(c1 == '(' and c2 == ')'):
            return True
        if(c1 == '[' and c2 == ']'):
            return True
        if(c1 == '{' and c2 == '}'):
            return True
        return False

    def isValid(self, s: str) -> bool:
        st = []
        for character in s:
            if(len(st) != 0):
                li = st[-1]
                if(self.isEqual(li, character)):
                    st.pop()
                    continue
            st.append(characrer)
        return len(st) == 0
