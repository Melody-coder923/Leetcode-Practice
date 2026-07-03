1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        if not digits:
4            return []
5        #Step1: 做字典
6        map={ "2":"abc",
7        "3": "def",
8        "4": "ghi",
9        "5": "jkl",
10        "6": "mno",
11        "7": "pqrs",
12        "8": "tuv",
13        "9": "wxyz"}
14        res=[]
15        def backtrack(idx,path):
16            if idx==len(digits):
17                res.append("".join(path[:]))
18                return 
19            for letter in map[digits[idx]]:
20                path.append(letter)
21                backtrack(idx+1,path)
22                path.pop()
23        backtrack(0,[])
24        return res