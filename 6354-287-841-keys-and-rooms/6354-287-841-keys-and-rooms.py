class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        roomsOpened = set()

        def dfs(room, curKeys):
            nonlocal roomsOpened
            if len(curKeys) == 0:
                return

            if room in curKeys:
                roomsOpened.add(room)
                curKeys.remove(room)
                for each in rooms[room]:
                    if each not in roomsOpened:
                        curKeys.append(each)
            
            for each in curKeys:
                dfs(each, curKeys)

        dfs(0, [0])
        print(roomsOpened)
        if len(roomsOpened) == len(rooms):
            return True
        else:
            return False
        