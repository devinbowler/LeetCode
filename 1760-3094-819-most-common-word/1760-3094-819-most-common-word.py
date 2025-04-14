class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuation = ".,!?;:'\"-()[]{}"
        cleanWord = ""
        for char in paragraph:
            if char not in punctuation:
                cleanWord += char
            else:
                cleanWord += " "

        words = cleanWord.lower().split()
        freq = Counter(words)
        inOrder = freq.most_common()

        for key, val in inOrder:
            if key not in banned:
                return key