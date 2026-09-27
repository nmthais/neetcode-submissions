import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        stack = []
        res = 0

        for i in range(len(tokens)):
            if tokens[i].isalnum() or (tokens[i].startswith('-') and tokens[i][1:].isalnum()):
                stack.append(tokens[i])
            else:
                res = int(map[tokens[i]](int(stack[-2]), int(stack[-1])))
                stack.pop(-2)
                stack.pop(-1)
                stack.append(res)
        
        return res if res!=0 else int(stack.pop())