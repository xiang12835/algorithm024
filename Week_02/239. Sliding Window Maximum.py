class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        暴力法
        时间复杂度：O(n * k)
        """ 

        if not nums:
            return []
        
        n = len(nums)
        r = []
        for i in range(n-k+1):
            window = nums[i:i+k]
            r.append(max(window))
        return r
        

class Solution1(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        大顶堆

        T: O(nlogn)
        S: O(n)
        """ 

        import heapq

        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:  
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans
