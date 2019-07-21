import math

class Heap(Object):
    def __init__(self, _type = 'max'):
        self.arr = []
        self.size = 0
        self._type = _type if _type == 'max' else 'min'

    def __repr__(self):
        return str(self.arr)

    '''
        Returns Parent index given a index
    '''
    def parent(self, index):
        return math.ceil((index-1)/2)

    '''
        Returns left child index given a index
    '''
    def left_child(self, index):
        return 2*index + 1

    '''
        Returns right child index given a index
    '''
    def right_child(self, index):
        return 2*index + 2


    '''
        Returns min/max element from the heap
    '''
    def get(self):
        return self.arr[0]

    '''
        Inserts new element in heap
    '''
    def insert(self, element):
        self.arr.append(element)
        self.size += 1

        if self.size == 1:
            return


        self_index = self.size - 1
        parent_index = self.parent(self_index)

        #Move new element upward untill you reach root and you find a smaller element as its parent
        while parent_index != self_index and ((self._type == 'max' and self.arr[parent_index] < self.arr[self_index]) or (self._type == 'min' and self.arr[parent_index] > self.arr[self_index])):
            self.arr[parent_index], self.arr[self_index] = self.arr[self_index], self.arr[parent_index]

            self_index = parent_index
            parent_index = self.parent(parent_index)

    '''
        removes max/min element from heap
    '''
    def remove(self):
        if self.size == 0:
            return

        #Swap the last element with root
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]

        #Remove the last element
        element = self.arr.pop(-1)
        self.size -= 1

        #Make sure heap maintains the heap property and go downwards
        parent_index = 0
        left_index = 1
        right_index = 2

        #Check if there is any left child, No need to check right child at the moment as it should be a complete binary tree
        while left_index < self.size:
            if right_index < self.size and ((self._type == 'max' and self.arr[right_index] > self.arr[left_index]) or (self._type == 'min' and self.arr[right_index] < self.arr[left_index])):
                index = right_index
            else:
                index = left_index

            #Swap
            if (self._type == 'max' and self.arr[index] > self.arr[parent_index]) or (self._type == 'min' and self.arr[index] < self.arr[parent_index]):
                self.arr[index], self.arr[parent_index] = self.arr[parent_index], self.arr[index]

            parent_index = index
            left_index = self.left_child(parent_index)
            right_index = self.right_child(parent_index)


        return element
