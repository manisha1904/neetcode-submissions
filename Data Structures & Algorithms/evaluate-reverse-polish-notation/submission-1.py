def evaluate(num1: int, num2: int, operator: str) -> int:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    return int(num1 / num2)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        length = len(tokens)
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                second_num = st[-1]
                st.pop()
                first_num = st[-1]
                st.pop()
                result = evaluate(first_num, second_num, token)
                st.append(result)
            else:
                st.append(int(token))
        
        return st[-1]
