class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        def checkRes(str, index, length, string):
            if index == length:
                return True

            # print(str, str1[index:index + len(str)])
            if string[index:index + len(str)] == str:
                newIndex = index + len(str)
                return checkRes(str, newIndex, length, string)

        length = min(len(str1), len(str2))
        check = max(len(str1), len(str2))
        for index in range(length):
            if str1[index] == str2[index]:
                if check % len(str1[:index + 1]) == 0:
                    testStr = str1[:index + 1]
                    if checkRes(testStr, len(testStr), len(str1), str1) and checkRes(testStr, len(testStr), len(str2), str2):
                        res = testStr
                    else:
                        continue

        return res