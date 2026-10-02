class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPos = [(p, s) for p, s in zip(position, speed)]
        sortedPos.sort(reverse=True)
        
        count = 1
        prevTime = (target - sortedPos[0][0])/sortedPos[0][1]
        for i in range(1, len(sortedPos)):
            time = (target - sortedPos[i][0])/sortedPos[i][1]
            if time > prevTime:
                count+=1
                prevTime = time

        return count