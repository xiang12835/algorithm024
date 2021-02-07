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

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        法二：去构建一个大顶堆，然后去删除k次，取k个最大值

        T: O(nlogn)
        S: O(n)
        """
        import collections, heapq

        d = collections.Counter(nums)
        hp, ans = [], []
        for i in d:
            heapq.heappush(hp, (-d[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(hp)[1])  # 每删除一个都需要调整堆
        return ans


