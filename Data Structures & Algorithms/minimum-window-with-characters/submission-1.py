class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t
        l = 0
        
        freq1 = {}
        freq2 = {}
        for i in t:
            freq2[i] = 1+ freq2.get(i,0)
        have = 0
        need = len(freq2)
        res = [-1,-1]
        resLen = 100001   
        for r in range(len(s)):
            freq1[s[r]] = 1+ freq1.get(s[r],0)
            if s[r] in freq2 and freq2.get(s[r]) == freq1.get(s[r]):
                have+=1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                freq1[s[l]] -= 1
                if s[l] in freq2 and freq1[s[l]] < freq2[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != 100001 else ""