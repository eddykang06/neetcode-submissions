class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            
            # Store row and column
            row = board[i]
            col = [arr[i] for arr in board]

            # Initialize a hashmap to count instances of characters
            hash_row = {}
            hash_col = {}

            for i in range(len(row)):
                
                # Store counts for non empty squares in row
                if row[i] != ".":
                    hash_row[row[i]] = hash_row.get(row[i], 0) + 1
                    if hash_row[row[i]] > 1:
                        return False
                
                # Store counts for non empty squares in column
                if col[i] != ".":
                    hash_col[col[i]] = hash_col.get(col[i], 0) + 1
                    if hash_col[col[i]] > 1:
                        return False
        
        # Iterate through each 3x3 square
        for k in range(0, 9, 3):
            for m in range(0, 9, 3):

                # Store squares in 3x3 box
                box = [row[m:m+3] for row in board[k:k+3]]
                box = [item for sublist in box for item in sublist]

                # Construct hashmap 
                hash_box = {}

                for i in range(len(box)):
                    # Store counts for non empty squares in box
                    if box[i] != ".":
                        hash_box[box[i]] = hash_box.get(box[i], 0) + 1
                        if hash_box[box[i]] > 1:
                            return False
        
        return True
        

