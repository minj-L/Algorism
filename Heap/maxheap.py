class MaxHeap(object):

    def __init__(self):
        self.queue = []

    # 새로운 노드 삽입 시 부모노드와 값 비교
    def insert(self, n):
        self.queue.append(n)
        last_index = len(self.queue) - 1
        if last_index < 0:
            return -1
        parent_index = self.parent(last_index)
        
        while 0 <= last_index:
            if 0 <= last_index and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break
    
    # 가장 위 루트 노드가 삭제 된다.(제일 큰 수)    
    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            return -1
        self.swap(0, last_index) # 루트 노트가 pop 되면 가장 마지막 노드를 루트 노드에 넣은 뒤 값을 비교해 가며 재정렬 한다.
        maxv = self.queue.pop() # 맨 마지막에 위치한 max값 출력
        self.maxHeapify(0)
        print(maxv)
        return maxv
        
    def maxHeapify(self, i):
        left_index = self.leftChild(i)
        right_index = self.rightChild(i)
        max_index = i

        if left_index <= len(self.queue) -1 and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
        if right_index <= len(self.queue) -1 and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index
        
        if max_index != i:
            self.swap(i, max_index)
            self.maxHeapify(max_index)

    def parent(self, index):
        return (index - 1) // 2
    
    def swap(self, index, parent_index):
        self.queue[index], self.queue[parent_index] = self.queue[parent_index], self.queue[index]

    def leftChild(self, index):
        return index * 2 + 1
    
    def rightChild(self, index):
        return index * 2 + 2
    
    def printHeap(self):
        print(self.queue)

if __name__=="__main__":
    mh = MaxHeap()
    mh.insert(1)
    mh.insert(3)
    mh.insert(11)
    mh.insert(6)
    mh.insert(5)
    mh.insert(2)
    mh.printHeap()
    mh.delete()
    mh.printHeap()

    