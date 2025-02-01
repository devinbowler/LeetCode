class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        sArr = list(s)
        arrIdx = 0
        flag = False

        for index in range(len(s)):
            if sArr[index] != " ":
                flag = True
                if len(res) <= arrIdx:
                    res.append("")
                    res[arrIdx] += sArr[index]
                else:
                    res[arrIdx] += sArr[index]
            else:
                if flag == True:
                    arrIdx += 1
                    flag = False

        res.reverse()
        return " ".join(res)