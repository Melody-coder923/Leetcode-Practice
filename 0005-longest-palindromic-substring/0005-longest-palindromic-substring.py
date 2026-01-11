class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Step1: 判断是不是回文 , 返回回文
        # Step2: 奇数和偶数分别出发
        def is_Palindrom(left,right):
            if left<0 or right>=len(s):
                return ""
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            #终止条件是 b a b  
            #          0 1 2
            #       -1       3
            return s[left+1:right]
        res=""
        max_len=float("-inf")
        for i in range(len(s)):
            s1=is_Palindrom(i,i)
            s2=is_Palindrom(i,i+1)
            if len(s1)>max_len:
                res=s1
                max_len=len(s1)
            if len(s2)>max_len:
                res=s2
                max_len=len(s2)
        return res


        