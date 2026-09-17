class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        windowLen = len(s1)
        temp1 = [x for x in s1]
        temp2 = [s2[x] for x in range(windowLen)]
        if sorted(temp1) == sorted(temp2):
            return True
        l = 0
        for r in range(windowLen, len(s2)):
            if (r - l + 1) > windowLen:
                temp2.remove(s2[l])
                l+=1
            temp2.append(s2[r])
            if sorted(temp1) == sorted(temp2):
                return True
            
        return False