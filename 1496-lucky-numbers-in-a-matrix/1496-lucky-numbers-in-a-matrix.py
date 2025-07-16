class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Okay I mean brute force is just element by element check its 
        # row and column and if its satisfying both add it to a return
        # array.
        finalArray = []

        for i in range(len(matrix)):
            row = matrix[i]
            min_val = min(row)
            min_col_index = row.index(min_val)

            is_max_in_col = True
            for j in range(len(matrix)):
                if matrix[j][min_col_index] > min_val:
                    is_max_in_col = False
                    break
            
            if is_max_in_col:
                finalArray.append(min_val)
        
        return finalArray
                