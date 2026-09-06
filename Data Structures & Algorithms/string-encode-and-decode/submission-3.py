class Solution:

    def encode(self, strs: List[str]) -> str:
        result: str = ""
        for string in strs:
            result += f"{len(string)}#{string}"
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        length = len(s)
        print(s)
        pointer = 0
        while pointer <length:
            ndpointer = pointer 
            while s[ndpointer] != "#":
                ndpointer +=1
            print(ndpointer)
            lengthWord = int(s[pointer:ndpointer])
            word = s[ndpointer+1:ndpointer+lengthWord +1]
            result.append(word)
            pointer = ndpointer + lengthWord +1
        return result