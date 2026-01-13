class Solution:
    def maxScore(self, s: str) -> int:
        # left 0  i   right 1
        # score= left_zero+right_one
        # left_zero : scan count if c==0 left_zero+=1  !!!
        # left_one :scan count if c==1 left_one+=1
        # right_one= total_one-left_one     !!!
        # maxSocre= max(score, maxScore)
        left_one,left_zero=0,0
        total_one=s.count("1")
        maxScore=0
        for c in s:
            if c=="0":
                left_zero+=1
            else:
                left_one+=1
            right_one=total_one-left_one
            score=left_zero+right_one
            maxScore=max(maxScore,score)
        return maxScore