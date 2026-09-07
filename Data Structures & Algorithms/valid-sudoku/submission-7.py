class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        for i in range(len(board)):
            seenSet = set()
            for j in range(len(board[i])):
                tempLen = len(seenSet)
                if board[i][j].isdigit():
                    seenSet.add(board[i][j])
                    if len(seenSet) == tempLen:
                        valid = False
                        return valid
        for j in range(len(board)):
            seenSet = set()
            for i in range(len(board[j])):
                tempLen = len(seenSet)
                if board[i][j].isdigit():
                    seenSet.add(board[i][j])
                    if len(seenSet) == tempLen:
                        valid = False
                        return valid
        for sqr in range(9):
            seenSet = set()
            for i in range(3):
                for j in range(3):
                    row = (sqr // 3) * 3 + i
                    col = (sqr % 3) * 3 + j
                    tempLen = len(seenSet)
                    if board[row][col].isdigit():
                        seenSet.add(board[row][col])
                        if len(seenSet) == tempLen:
                            valid = False
                            return valid
                
        return valid

       