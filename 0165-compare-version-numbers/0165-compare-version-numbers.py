class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = j = 0
        n1, n2 = len(version1), len(version2)

        while i < n1 or j < n2:
            num1 = 0
            while i < n1 and version1[i] != '.':
                num1 = num1 * 10 + (ord(version1[i]) - 48)  # faster than int()
                i += 1

            num2 = 0
            while j < n2 and version2[j] != '.':
                num2 = num2 * 10 + (ord(version2[j]) - 48)
                j += 1

            if num1 > num2:
                return 1
            if num1 < num2:
                return -1

            # 只有当当前字符是 '.' 才跳过它
            if i < n1 and version1[i] == '.':
                i += 1
            if j < n2 and version2[j] == '.':
                j += 1

        return 0