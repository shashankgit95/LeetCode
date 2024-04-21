class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        hm = {}
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1
        for c in t:
            if c not in hm or hm[c] == 0:
                return False
            else:
                hm[c] -= 1
        return True