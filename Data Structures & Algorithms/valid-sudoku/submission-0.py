class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for i in range(9):
            st = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if int(board[i][j]) in st:
                    return False
                st.add(int(board[i][j]))

        # col check
        for i in range(9):
            st = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if int(board[j][i]) in st:
                    return False
                st.add(int(board[j][i]))
        
        # box check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                st = set()
                for x in range(i, i+3, 1):
                    for y in range(j, j+3, 1):
                        if board[x][y] == '.':
                            continue
                        if int(board[x][y]) in st:
                            return False
                        st.add(int(board[x][y]))
        return True