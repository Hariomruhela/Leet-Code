class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        def check(k):
            data=[0]*(n+1)
            for query in queries[:k]:
                l,r,val=query
                data[l]=data[l]+val
                data[r+1]=data[r+1]-val
            for i in range(1, len(data)):
                data[i]=data[i]+data[i-1]
            for i,j in zip(data, nums):
                if i<j:
                    return False
            return True


        if not check(len(queries)):
            return-1
        l=0
        r=len(queries)

        while l<=r:
            mid=(l+r)//2
            if check(mid):
                r=mid-1
            else:
                l=mid+1
        return l