class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        length = len(temperatures)
        result = [0] * length 

        for i in range(length-1, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()
            result[i] = (st[-1] - i) if st else 0
            st.append(i)
        
        return result
