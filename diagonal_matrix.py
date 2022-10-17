class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        result = []  #to append the numbers from the matrix
        m = len(mat)  #length of the matrix is to calculate the number of rows
        n = len(mat[0])  #len of the matrix[0] is to calculate number of columns
        
        result = [0]*(m*n)  #to append the numbers from the matrix
        flag = 1  #flag is to go down and to come up
        index = 0  
        
        r = 0  #row no
        c = 0  #column no
        
        while(index < len(result)):  #itertate through the matrix
            result[index] = mat[r][c]  #appending the numbers from the matrix to the list
            if flag ==1:  #if the flag variable is one we are in up position
                if c == n-1:  #if we the column value is equal to the last column we are incrementing the row and setting the flag to -1
                    r+=1
                    flag =-1
                elif r==0:  #if the above condition fails, we are checking whether we are in 0th row, if we are in 0th row we are incrementing the column and setting flag to -1
                    c+=1
                    flag=-1
                else:   #else we are incrementing the column and decrementing the row
                    r-=1
                    c+=1

            else:   #if flag is not one we are going to do down operation
                if r ==m-1:  #if the row hits the last row we are incrementing the column
                    c+=1
                    flag =1  # and we are setting the flag to 1
                elif c ==0:  #if the index is in the 0th column we are incrementing the row and setting the flag to 1
                    r+=1   
                    flag = 1
                else:  #else we are continuing the down operation
                    c-=1
                    r+=1

            index+=1  #we are incrementing the index
                        
        return result
                        
            
        
        
        