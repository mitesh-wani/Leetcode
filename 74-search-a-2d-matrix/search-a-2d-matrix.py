class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        itr=m
        n=len(matrix[0])
        i=0
        while itr >i:
            low=0
            high=n-1
            arr=matrix[i]
            i=i+1
            while low<=high:
                mid=low+(high-low)//2
                print(mid)
                if arr[mid]==target:
                    return True
                elif arr[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
        return False