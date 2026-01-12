class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 最长-> 过程比较取最长 ->满足回文
        n=len(s)
        # Step1: 判断是不是回文 function->返回回文的字符串
        def is_Palindrom(left,right):
            if left<0 or right>=n:
                return ""
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        # Step2: 比较最长 : 情况1:  baab  i,i+1 情况2 bab  i,i
        maxLen=0
        res=""
        for i in range(n):
            s1=is_Palindrom(i,i+1)
            s2=is_Palindrom(i,i)
            if len(s1)>maxLen:
                maxLen=len(s1)
                res=s1
            if len(s2)>maxLen:
                maxLen=len(s2)
                res=s2
        return res