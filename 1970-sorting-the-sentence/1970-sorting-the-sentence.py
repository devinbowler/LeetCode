class Solution:
    def sortSentence(self, s: str) -> str:
        # Okay so just loop through and track each word up util its number
        # store it in a already made array, then concat
        wordArr = [None] * 10
        returnSentance = ""
        firstWord = True

        curWord = ""
        for char in s:
            if char.isdigit():
                wordArr[int(char)] = curWord
                curWord = ""
            if char is not " " and not char.isdigit():
                curWord += char
        
        for idx, each in enumerate(wordArr):
            if each is not None:
                if firstWord:
                    returnSentance += each
                    firstWord = False
                else:
                    returnSentance += (" " + each)
    
        return returnSentance
