class Solution:
    def removeStars(self, s: str) -> str:
        arrInp = list(s)
        stack = []

        for each in arrInp:
            if each != '*':
                stack.append(each)
            else:
                stack.pop()

        return "".join(stack)
