class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def add(self, priority, item):
        self.heap.append((priority, item))
        self._bubble_up(len(self.heap) - 1)

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def pop_min(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        self._bubble_down(0)
        return min_item

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _bubble_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.heap[index][0] < self.heap[parent][0]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _bubble_down(self, index):
        length = len(self.heap)
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            smallest = index

            if left < length and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < length and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest == index:
                break
            self._swap(index, smallest)
            index = smallest


class PriorityQueue:
    def __init__(self):
        self.min_heap = MinHeap()

    def push(self, item, priority):
        self.min_heap.add(priority, item)

    def pop(self):
        result = self.min_heap.pop_min()
        return result[1] if result else None

    def peek(self):
        result = self.min_heap.peek()
        return result[1] if result else None

    def is_empty(self):
        return self.min_heap.is_empty()
