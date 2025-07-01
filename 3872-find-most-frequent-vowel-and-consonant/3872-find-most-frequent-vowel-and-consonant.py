class Solution:
    def maxFreqSum(self, s: str) -> int:
        # I need to make a counter just for the vowls, then just for all other letters.
        # Then sort them both and add the top values together and return it.
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelCount, consonantCount = [], []

        for char in s:
            if char in vowels:
                vowelCount.append(char)
            else:
                consonantCount.append(char)
        
        vowelCount, consonantCount = Counter(vowelCount), Counter(consonantCount)
        vowelCount = dict(sorted(vowelCount.items(), key=lambda x: x[1], reverse=True))
        consonantCount = dict(sorted(consonantCount.items(), key=lambda x: x[1], reverse=True))

        topVowel = list(vowelCount.items())[0][1] if vowelCount else 0
        consonantCount = list(consonantCount.items())[0][1] if consonantCount else 0

        return topVowel + consonantCount