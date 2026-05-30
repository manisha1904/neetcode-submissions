class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        brackets_dict = {')' : '(', '}' : '{', ']' : '['}
        length = len(s)
        for ch in s:
            if st and ch not in brackets_dict.values():
                open_bracket = brackets_dict[ch]
                if st[-1] != open_bracket:
                    return False
                st.pop()
                continue
            st.append(ch)
        return not len(st)