1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        #Step1: 做字典
4        d_to_l={ "2":"abc",
5        "3": "def",
6        "4": "ghi",
7        "5": "jkl",
8        "6": "mno",
9        "7": "pqrs",
10        "8": "tuv",
11        "9": "wxyz"}
12        res=[]
13        def backtrack(path,idx):
14            if idx==len(digits):
15                res.append("".join(path[:]))
16                return
17            
18            for letter in d_to_l[digits[idx]]:
19                path.append(letter)
20                backtrack(path,idx+1)
21                path.pop()
22            return
23
24        backtrack([],0)
25        return res
26