class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        finalList = []
        groupDict = {}
        for person, size in enumerate(groupSizes):
            if size in groupDict:
                groupDict[size].append(person)
            else:
                groupDict[size] = [person]
            
            if len(groupDict[size]) == size:
                finalList.append(groupDict[size])
                groupDict[size] = []

        for size, people in groupDict.items():
            if len(people) > 0:
                finalList.append(people)

        return finalList 
