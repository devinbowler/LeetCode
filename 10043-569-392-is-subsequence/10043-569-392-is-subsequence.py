class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if t == "":
            return False
        idx, arrT, arrS = 0, list(t), list(s)
        
        for each in arrT:
            if arrS[idx] == each:
                idx += 1
                if idx == len(arrS):
                    return True
        
        return False