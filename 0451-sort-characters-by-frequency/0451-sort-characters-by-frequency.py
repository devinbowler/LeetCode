class Solution:
    def frequencySort(self, s: str) -> str:
        # Okay so captial and lowercase are not the same and all we want is to re
        # make the string based off freq, so legit just make a freq dictionary
        # and loop through in appending it to a string then return it.
        # I can just use a counter.
        returnString = ''
        freqDict = Counter(s)
        sortedFreq = sorted(freqDict.items(), key=lambda x: -x[1])
        
        # Assemble the string
        for char, freq in sortedFreq:
            returnString += char * freq
        
        return returnString
        