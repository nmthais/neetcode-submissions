class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubs=0
        hasSeen = set()
        i = 0
        for j in range(len(s)):
            while s[j] in hasSeen:
                hasSeen.remove(s[i])
                i+=1
                
            hasSeen.add(s[j])
            longestSubs = max(longestSubs, j - i + 1)
        return longestSubs