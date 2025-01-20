import random


class Sort:
    def __init__(self, n):
        """
        n是排序的数的数量
        :param n:
        """
        self.len = n
        self.arr = [0] * n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def partition(self, low, high):
        # random_pos = random.randint(low, high)
        # self.arr[random_pos], self.arr[high] = self.arr[high], self.arr[random_pos]
        pivot = self.arr[low]
        while low < high:
            while low < high and self.arr[high] >= pivot:
                high -= 1
            self.arr[low] = self.arr[high]
            while low < high and self.arr[low] <= pivot:
                low += 1
            self.arr[high] = self.arr[low]
        self.arr[low] = pivot
        return low

    def partition2(self, low, high):
        arr = self.arr
        k = i = low
        random_pos = random.randint(low, high)
        arr[random_pos], arr[high] = arr[high], arr[random_pos]
        for i in range(low, high):
            if arr[i] < arr[high]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
            arr[k], arr[high] = arr[high], arr[k]
        return k

    def quick_sort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.quick_sort(low, pivot - 1)
            self.quick_sort(pivot + 1, high)

    def adjust_max_heap(self, pos, arr_len):
        """
        把某个子树调整为大根堆
        :param pos: 被调整的元素的位置
        :param arr_len: 当前列表总长度
        :return:
        """
        arr = self.arr
        dad = pos
        son = 2 * dad + 1
        while son < arr_len:  # 左孩子小于列表长度
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 判断右孩子是否存在，且右孩子是否大于左孩子
                son += 1
            if arr[son] > arr[dad]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):
        """
        堆排序
        :return:
        """
        # range(第一个非叶节点, 根节点（此处的-1代表的是根节点）, 从后往前遍历)
        for parent in range(self.len // 2 - 1, -1, -1):
            self.adjust_max_heap(parent, self.len)

        arr = self.arr
        for arr_len in range(self.len - 1, 0, -1):
            arr[0], arr[arr_len] = arr[arr_len], arr[0]
            self.adjust_max_heap(0, arr_len)


if __name__ == '__main__':
    s = Sort(10)
    # s.quick_sort(0, 9)
    s.heap_sort()
    pass
