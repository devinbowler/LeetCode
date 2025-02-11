class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        freq1, freq2 = Counter(word1), Counter(word2)

        values1, values2 = list(freq1.values()), list(freq2.values())

        keys1, keys2 = set(sorted(freq1.keys())), set(sorted(freq2.keys()))

        if keys1 != keys2:
            return False

        values1.sort(), values2.sort()
        for index in range(len(values1)):
            if values1[index] != values2[index]:
                return False

        return True