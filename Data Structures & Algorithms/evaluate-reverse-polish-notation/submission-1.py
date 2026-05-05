import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+' : operator.add , '-' : operator.sub , '*' : operator.mul, '/' : operator.truediv}

        for t in tokens:
            if (t not in operators):
                stack.append(int(t))
            else:
                second = stack.pop()
                first = stack.pop()
                result = operators[t](first,second)
                stack.append(int(result))
        return stack [-1]



