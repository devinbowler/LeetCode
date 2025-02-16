class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()
        for i,c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        while R and D:
            one = R.popleft()
            two = D.popleft()
            if one < two:
                R.append(one + len(senate))
            else:
                D.append(two + len(senate))
        return 'Radiant' if R else 'Dire'