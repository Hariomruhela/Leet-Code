class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_map={n:i for i,n in enumerate(arr)}
        res=0
        dp=[[0]*len(arr) for _ in range(len(arr))]

        for i in reversed(range(len(arr)-1)):
            for j in reversed(range(i+1, len(arr))):
                prev, cur=arr[i], arr[j]
                nxt= prev + cur
                length=2
                if nxt in arr_map:
                    length=1+dp[j][arr_map[nxt]]
                    res=max(res, length)
                    
                dp[i][j]=length
        return res


        