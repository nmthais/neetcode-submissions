class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = 1
        res = []
        indexMaxTemp=-1
        maxTemp = 0
        for l in range(len(temperatures)-1,-1,-1):
            maxTemp = max(maxTemp, temperatures[l])
            
            if maxTemp == temperatures[l]:
                indexMaxTemp = l
                res.append(0)
            else:
                r = l+1
                while r < indexMaxTemp and temperatures[l] >= temperatures[r]:
                    r+=1
                if temperatures[r] == maxTemp:
                    res.append(indexMaxTemp - l)
                else:
                    res.append(r-l)
        res.reverse()
        return res