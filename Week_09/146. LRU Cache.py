import collections
class LRUCache(object):
    """
    双向链表中，在后面的节点表示被最近访问
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        
        OrderedDict.popitem()有一个可选参数last（默认为True），当last为True时它从OrderedDict中删除最后一个键值对并返回该键值对，当last为False时它从OrderedDict中删除第一个键值对并返回该键值对。
        """
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)  # 头删尾插
        self.dic[key] = value  # 头删尾插


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)