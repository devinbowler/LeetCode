# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def makeInt(node, num):
            if not node:
                return num
            
            num.append(node.val)
            return makeInt(node.next, num)

        def makeList(index, array, listHead):
            if index >= len(array):
                return listHead

            newNode = ListNode(array[index])
            newNode.next = listHead
            listHead = newNode
            
            return makeList(index + 1, array, listHead)

            

        return1 = makeInt(l1, [])
        return2 = makeInt(l2, [])

        correctNum1 = list(reversed(list(return1)))
        correctNum2 = list(reversed(list(return2)))

        num1 = int("".join(map(str, correctNum1)))
        num2 = int("".join(map(str, correctNum2)))

        result = num1 + num2
        print("Number 1: ", num1, ". Number 2: ", num2, ". Sum: ", result)
        res = list(map(int, str(result)))
        listRes = ListNode(res[0])
        print(res)

        return makeList(1, res, listRes)


