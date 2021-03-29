class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        方法：栈

        T：O(n)，因为我们一次只遍历给定的字符串中的一个字符并在栈上进行 O(1) 的推入和弹出操作。
        S：O(n)，当我们将所有的开括号都推到栈上时以及在最糟糕的情况下，我们最终要把所有括号推到栈上。例如 (((((。
        """
        stack = []
        d = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in d: # 右括号
                if not stack or stack[-1] != d[c]:  # case1: ] case2: [}
                    return False
                stack.pop()
            else:  # 左括号
                stack.append(c)
        
        return not stack
