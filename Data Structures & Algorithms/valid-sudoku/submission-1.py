from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #For validating rows
        for i in range(9):
            s = set()
            for j in range(9):
                box = board[i][j]
                if box in s:
                    return False
                elif box != ".":
                    s.add(box)

        #For validating columns
        for i in range(9):
            s = set()
            for j in range(9):
                box = board[j][i]
                if box in s:
                    return False
                elif box != ".":
                    s.add(box)

        #For validating 9x9 grid
        starts = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6, 0), (6,3), (6,6)]

        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for column in range(j, j+3):
                    box = board[row][column]
                    if box in s:
                        return False
                    elif box != ".":
                        s.add(box)
        return True
        
        



        
        
                
        
            
    
            
    