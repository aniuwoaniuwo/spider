#-*-coding:utf-8-*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        net = 0
        sums = []
        j = len(l2)
        i = len(l1)
        print(i,j)
        if i < j:
            for k in range(i, j):
                l1.append(0)
        else:
            for k in range(j, i):
                l2.append(0)
        for h in range(len(l1)):
            sum = l1[h] + l2[h] + net
            net = 0
            if sum > 9:
                sum = sum - 10
                net = 1
            sums.append(sum)
        if net == 1:
            sums.append(net)
        print(sums)
        return sums



if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    ff = Solution()
    ff.addTwoNumbers(l1, l2)