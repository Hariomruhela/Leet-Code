class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum=0
        odd_cnt=0
        even_cnt=0
        res=0
        MOD=10**9 + 7

        for n in arr:
            cur_sum+=n

            if cur_sum %2:
                res=(res+1+even_cnt)%MOD
                odd_cnt+=1
            else:
                res=(res+odd_cnt)%MOD
                even_cnt+=1
        return res      