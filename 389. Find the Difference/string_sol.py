class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in s:
            t.remove(i)
        return t[0]