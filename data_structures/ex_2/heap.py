def heapsort(arr):
    # create a heap and assign it to a variable
    heap = Heap()
    # create an empty list to append to
    sorted_list = []
    # for every item in the array passed in as an argument,
    # insert the item into the heap variable
    for num in arr:
        heap.insert(num)
    # while the size of the heap is greater than 0,
    # insert the return from heap.delete
    # to the first index of the sorted_list
    while heap.size > 0:
        # sorted_list = [heap.delete()] + sorted
        sorted_list.insert(0, heap.delete())
    # return the sorted list
    return sorted_list


# heapsort given in solution lecture
# def heapsort(arr):
#     heap = Heap()
#     sorted = [0] * len(arr)

#     for el in arr:
#         heap.insert(el)

#     for i in range(len(arr)):
#         sorted[len(arr) - i - 1] = heap.delete()

#     return sorted


class Heap:
    def __init__(self):
        self.storage = [0]
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        self._bubble_up(self.size)

    def delete(self):
        retval = self.storage[1]
        self.storage[1] = self.storage[self.size]
        self.size -= 1
        self.storage.pop()
        self._sift_down(1)
        return retval

    def get_max(self):
        return self.storage[1]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        while index // 2 > 0:
            if self.storage[index // 2] < self.storage[index]:
                self.storage[index], self.storage[index // 2] = (
                    self.storage[index // 2],
                    self.storage[index],
                )
            index = index // 2

    def _sift_down(self, index):
        while (index * 2) <= self.size:
            mc = self._max_child(index)
            if self.storage[index] < self.storage[mc]:
                self.storage[index], self.storage[mc] = (
                    self.storage[mc],
                    self.storage[index],
                )
            index = mc

    def _max_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            return (
                index * 2
                if self.storage[index * 2] > self.storage[index * 2 + 1]
                else index * 2 + 1
            )
