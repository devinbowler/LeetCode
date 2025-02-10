class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqMap = {}
        values = []
        for each in arr:
            if each in freqMap:
                freqMap[each] += 1
            else:
                freqMap[each] = 1

        for key, value in freqMap.items():
            values.append(value)
        
        setArr = set(values)

        if len(setArr) == len(values):
            return True
        else:
            return False