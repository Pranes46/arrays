class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)  #to know the number of rows
        n = len(matrix[0])  #to know the number of columns
        
        left = 0  #keeping the left pointer at index 0  of 0th row
        right = n-1  #keeping the right pointer to the last index of the first row
        top = 0  #keeping the top pointer at 0th index of 0th row
        bottom = m-1  #keeping the bottom pointer at the last index of the matrix
        
        result = []
        
        while (left<=right and top<=bottom):  #if the top pointer crosses the bottom and left crosses the right the loop breaks
            
            #left to right
            
            for i in range(left,right+1):  #we gonna process the matrix from left to right and append it in the list
                result.append(matrix[top][i])  
            top+=1  # we are incrementing the top, means we are done with the respective row and we are changing top to the next row
                
            #top to bottom
            for j in range(top,bottom+1): #we gonna process the matrix from top to bottom and append it in the list
                result.append(matrix[j][right])  
            right-=1 # we are decrementing the right, means we are done with the respective column and we are changing right to the prev columnm
                
            if len(result) == (m*n):  #if the result is full we gonna break the loop
                break
                
            #right to left  
            for k in range(right,left-1,-1):  #we gonna process the matrix from top to bottom and append it in the list
                result.append(matrix[bottom][k])
            bottom-=1 
                
            #bottom to top
            
            for l in range(bottom,top-1,-1): #we gonna process the matrix from bottom to top and append it in the list
                result.append(matrix[l][left])
            left+=1
                
                
        return result  #returning result
                
            
        