class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 !=0:
            return False
        dictionary = {"(": ')', '{': '}', '[':']',}
        queue = []
        for i in s:
            if i in dictionary:
                queue.append(i)
            else:
                if len(queue) == 0 or i != dictionary[queue[len(queue)-1]]:
                    return False
                else:
                    queue.pop(len(queue)-1)
        return len(queue) == 0