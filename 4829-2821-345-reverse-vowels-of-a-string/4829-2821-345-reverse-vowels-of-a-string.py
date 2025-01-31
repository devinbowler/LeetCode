class Solution:
    def reverseVowels(self, s: str) -> str:
        sArr = list(s)
        left, right = 0, len(sArr) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while left < right: 
            if sArr[left] in vowels:
                if sArr[right] in vowels:
                    temp = sArr[left]
                    sArr[left] = sArr[right]
                    sArr[right] = temp
                    right -= 1
                    left += 1
                else:
                    right -= 1
            else:
                left += 1

        return "".join(sArr) 