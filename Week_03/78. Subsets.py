class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        迭代法
        """
        results = [[]]

        for num in nums:
            l = []
            for result in results:
                l.append(result+[num])

            results.extend(l)
        return results

class Solution1(object):

    """
    1.全部考虑，选或不选

    1选或不选，有两种情况，2选或不选，有两种情况，3选或不选，有两种情况，那么总共就是2\*2\*2=8种情况：

    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self._recursion([], 0, nums)
        return self.res

    def _recursion(self, l, index, nums):

        # terminator
        if index == len(nums):
            self.res.append(l)
            return

        # pick the number at this index
        self._recursion(l + [nums[index]], index + 1, nums)

        # not pick the number at this index
        self._recursion(l, index + 1, nums)

        # reverse the current state
