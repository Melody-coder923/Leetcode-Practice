class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        curSum=0
        res=0
        for num in nums:
            curSum+=num
            if curSum-k in dic:
                res+=dic[curSum-k]
            dic[curSum]+=1

        return res