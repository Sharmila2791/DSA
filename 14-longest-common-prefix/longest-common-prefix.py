class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        p=strs[0]
        ans=""
        for i in range(len(p)):
            c=p[i]
            for word in strs[1:]:
                if i ==len(word) or word[i] !=c:
                    return ans
            ans+=c
        return ans