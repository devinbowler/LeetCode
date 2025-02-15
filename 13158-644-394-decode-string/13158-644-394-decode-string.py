class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                substring = ''
                scaler = ''

                while stack and stack[-1] != '[':
                    substring = stack.pop() + substring

                stack.pop()

                while stack and stack[-1].isdigit():
                    scaler = stack.pop() + scaler

                res = int(scaler) * substring
                stack.extend(res)

                continue

            
            stack.append(char)

        return "".join(stack)