class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = {}
        for i in s:
            if i in seen:
                seen[i] = seen[i] + 1
            else:
                seen[i] = 1
        for i in t:
            if i not in seen.keys():
                return i
            letter = t.count(i)
            if letter != seen[i]:
                return i