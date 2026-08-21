class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class linked:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}
    
    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.right.prev = node
        node.prev.next = node
        self.map[val] = node
   
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)

    def popLeft(self):
        res = self.left.next.val;
        self.pop(res)
        return res

    def update(self, val):
        self.pop(val)
        self.pushRight(val)

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuC = 0
        self.valMap = {}
        self.countMap = defaultdict(int)
        self.ListMap = defaultdict(linked)

    def counter(self,key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.ListMap[cnt].pop(key)
        self.ListMap[cnt + 1].pushRight(key)

        if cnt == self.lfuC and self.ListMap[cnt].length() == 0:
            self.lfuC +=1


    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]
                

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.ListMap[self.lfuC].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)
        self.valMap[key] = value
        self.counter(key)
        self.lfuC = min(self.lfuC, self.countMap[key])
        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)