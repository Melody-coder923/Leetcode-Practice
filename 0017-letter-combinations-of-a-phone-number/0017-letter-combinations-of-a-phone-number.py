class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Step1: 做字典
        d_to_l={ "2":"abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}

        res=[]
        #Step2: 回溯
        def backtrack(path, idx):
            if idx==len(digits):
                res.append("".join(path))
                return
            
            for letter in d_to_l[digits[idx]]:
                path.append(letter)
                backtrack(path,idx+1)
                path.pop()  
        backtrack([],0)
        return res