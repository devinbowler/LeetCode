class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        res = []
        length = min(len(word1), len(word2))
        while index != length:
            res.append(word1[index])
            res.append(word2[index])
            index += 1
            
        if len(word1) != length:
            res.append(word1[index:])
        else:
            res.append(word2[index:])

        result = "".join(res)

        return result

        