class Solution:
    def compress(self, chars: List[str]) -> int:
        charCount = 1
        index = 1

        while index < len(chars):
            if chars[index] == chars[index - 1] and index != len(chars) - 1:
                charCount += 1
                del chars[index - 1]
            else:
                if chars[index] == chars[index - 1] and index == len(chars) - 1:
                    charCount += 1
                    del chars[index - 1]
                if charCount > 1:
                    for each in str(charCount):
                        chars.insert(index, each)
                        index += 1

                charCount = 1
                index += 1


        return len(chars)
            