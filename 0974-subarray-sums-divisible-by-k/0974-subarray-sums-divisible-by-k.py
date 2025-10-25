class Solution:
    from collections import defaultdict
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # non-empty
        # sum%k==0 
        #连续(prefix[i] - prefix[j-1]) % k == 0 =>prefix[i] % k == prefix[j-1] % k
        #如果两个前缀和 mod k 相等，那么它们之间的子数组和一定能被 k 整除
        # 我们记录每个余数 mod 出现的次数 prefix_mod[mod]
        mod_freq=defaultdict(int)
        mod_freq[0] = 1 # 初始化必须有,所有前缀和都是
        prefixsum=0
        res=0
        for num in nums:
            prefixsum+=num
            mod = (prefixsum % k + k) % k
            res += mod_freq[mod]
            mod_freq[mod]+=1
        return res
            
        
            