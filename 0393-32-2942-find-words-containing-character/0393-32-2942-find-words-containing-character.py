class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for index, each in enumerate(words):
            if x in list(each):
                result.append(index)

        return result
