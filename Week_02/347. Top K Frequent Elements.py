class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        字典 + 排序
        T: O(nlogn)
        S: O(n)
        """

        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        nums = list(set(nums))
        nums.sort(key=lambda n:d[n], reverse=True)
        return nums[:k]
        