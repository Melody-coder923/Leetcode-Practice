class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0]) # 3,4
        l,r=matrix[0][0],matrix[m-1][n-1]

        small,large=0,m*n-1
        
        while small<=large: 
            mid=small+(large-small)//2
            #index 5 ->11
            row= mid//n   #5//4=1
            col=mid%n    #5%4=1

            compare=matrix[row][col]

            if compare==target:
                return True
            elif compare<target:
                small=mid+1
            else:
                large=mid-1
        
        return False