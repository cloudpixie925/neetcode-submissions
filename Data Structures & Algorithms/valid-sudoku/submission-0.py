from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for array in board:
            count = Counter(array)
            for key, value in count.items():
                if value > 1 and key != ".":
                    return False
        for i in range(9):
            column = []
            for array in board:
                column.append(array[i])
            count_c = Counter(column)
            for key, value in count_c.items():
                if value > 1 and key != ".":
                    return False

        partitions = [[], [], [], [], [], [], [], [], []]

        for j in range(3):
            current = board[j]
            for k in range(3):
                if current[k] != "." and current[k] in partitions[0]:
                    return False
                else:
                    partitions[0].append(current[k])
        
        for j in range(3):
            current = board[j]
            for k in range(3,6):
                if current[k] != "." and current[k] in partitions[1]:
                    return False
                else:
                    partitions[1].append(current[k])
        
        for j in range(3):
            current = board[j]
            for k in range(6,9):
                if current[k] != "." and current[k] in partitions[2]:
                    return False
                else:
                    partitions[2].append(current[k])

        for j in range(3,6):
            current = board[j]
            for k in range(3):
                if current[k] != "." and current[k] in partitions[3]:
                    return False
                else:
                    partitions[3].append(current[k])

        for j in range(3,6):
            current = board[j]
            for k in range(3,6):
                if current[k] != "." and current[k] in partitions[4]:
                    return False
                else:
                    partitions[4].append(current[k])

        for j in range(3,6):
            current = board[j]
            for k in range(6,9):
                if current[k] != "." and current[k] in partitions[5]:
                    return False
                else:
                    partitions[5].append(current[k])

        for j in range(6,9):
            current = board[j]
            for k in range(3):
                if current[k] != "." and current[k] in partitions[6]:
                    return False
                else:
                    partitions[6].append(current[k])

        for j in range(6,9):
            current = board[j]
            for k in range(3,6):
                if current[k] != "." and current[k] in partitions[7]:
                    return False
                else:
                    partitions[7].append(current[k])

        for j in range(6,9):
            current = board[j]
            for k in range(6,9):
                if current[k] != "." and current[k] in partitions[8]:
                    return False
                else:
                    partitions[8].append(current[k])
        return True
        
        
                
        
            
    
            
    