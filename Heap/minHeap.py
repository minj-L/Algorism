class MinHeap(object):
    def __init__(self):
        self.queue = []

    def insert(self, n):
        self.queue.append(n)
        last_index = len(self.queue) - 1

        if last_index < 0 :
            return -1
        parent_index = self.parent(last_index)
        
        while 0 <= last_index:
            if 0 <= last_index and self.queue[last_index] < self.queue[parent_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break
    
    def delete(self):
        last_index = len(self.queue) -1
        if last_index < 0:
            return -1
        self.swap(0, last_index)
        minv = self.queue.pop()
        self.minheapyfiy(0)
        return minv

    def minheapyfiy(self, n):
        left_index = self.leftChilde(n)
        right_index = self.rightChild(n)
        min_index = n

        if left_index <= len(self.queue) -1 and self.queue[left_index] < self.queue[min_index]:
            min_index = left_index
        if right_index <= len(self.queue) -1 and self.queue[right_index] < self.queue[min_index]:
            min_index = right_index
        
        if min_index != n:
            self.swap(n, min_index)
            self.minheapyfiy(min_index)


    def parent(self, n):
        return (n - 1) // 2
    
    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def leftChilde(self, index):
        return (index * 2) + 1
    
    def rightChild(self, index):
        return (index * 2) + 2
    
    def printHeap(self):
        print(self.queue)

if __name__=="__main__":
    mh = MinHeap()
    mh.insert(1)
    mh.insert(3)
    mh.insert(11)
    mh.insert(6)
    mh.insert(5)
    mh.insert(2)
    mh.printHeap()
    mh.delete()
    mh.printHeap()
