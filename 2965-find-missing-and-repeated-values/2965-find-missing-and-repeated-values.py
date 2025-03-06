class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N=len(grid)
        count={}

        for i in range(N):
            for j in range(N):
                if grid[i][j] not in count:
                    count[grid[i][j]]=0
                count[grid[i][j]]+=1

        double, missing=0,0

        for num in range(1,N*N+1):
            if num not in count:
                missing =num
            elif count[num]==2:
                double=num
        return [double, missing]