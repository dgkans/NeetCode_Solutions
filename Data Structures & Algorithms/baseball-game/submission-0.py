class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i,v in enumerate(operations):
            if v == "C":
                stack.pop()
            elif v == "+":
                stack.append(stack[-1]+stack[-2])
            elif v == "D":
                stack.append(2* stack[-1])
            else:
                stack.append(int(v))
        return sum(stack)