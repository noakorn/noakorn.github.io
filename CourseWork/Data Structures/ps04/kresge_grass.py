

'''
BST partial implementation
'''

class Binary_Node():
    def __init__(self,val,i,size):
        self.val = val
        self.right = None
        self.left = None
        self.delta = 0
        self.index = i
        self.size = size

    def get_node(self, i) -> int:
        '''Return the i-th element in tree'''
        if self.index == i:
            return self.val + self.delta
        elif self.index < i:
            return self.right.get_node(i) + self.delta
        else:
            return self.left.get_node(i) + self.delta

    def increment_tree(self, a, b, k) -> None:
        '''Increment elements from indices a to b by k'''
        if self.size == b-a+1 and self.index == (b-a+1)//2:  # if [a:b] is simply the current tree
            self.delta += k
        elif a == b and a == self.index: # if we're only incrementing one
            self.val += k
        elif self.index > a and self.index == b:  # if we're currently at b, we need to increment part of the left subtree
            self.val += k
            self.left.increment_tree(a,b - 1,k)
        elif self.index == a and self.index < b:  # if we're currently at a, we need to increment part of the right subtree
            self.val += k
            self.right.increment_tree(a + 1, b, k)
        # now that we've covered the edge cases,
        # check if we're somewhere in the middle of the range
        # then recursively increment
        elif self.index > b: # if we're to the right of the range, increment only the left subtree
            self.left.increment_tree(a, b, k)
        elif self.index < a: # if we're to the left of the range, increment only the right subtree
            self.right.increment_tree(a, b, k)
        elif self.index > a and self.index < b:
            self.val += k
            self.left.increment_tree(a, self.index - 1, k)
            self.right.increment_tree(self.index + 1, b, k)


'''
Represents an array data structure which allows incrementing over
a range of indices. For example, if we started with an array:

A = [5, 1, 7, 2, 11]

Here are some example queries:
    get(0) --> 5
    get(1) --> 1
    get(2) --> 7
    get(3) --> 2
    get(4) --> 11

However, if we then called:
    increment(2, 4, 6) --> A = [5, 1, 13, 8, 17]
    increment(0, 3, 2) --> A = [7, 3, 15, 10, 17]

So the previous queries would now yield:
    get(0) --> 7
    get(1) --> 3
    get(2) --> 15
    get(3) --> 10
    get(4) --> 17
'''

def build_subtree(arr, start = 0, end = None):
    """
    builds the tree
    :param arr: the array
    :param c: constant to add to index
    :param end: end of array
    """

    def helper(start,end):
        mid = (end-start) // 2 + start
        root = Binary_Node(arr[mid], mid, end-start)  # where A[mid] is the value of our root
        if mid > start:  # need to store more items in left subtree
            root.left = helper(start, mid)
        if mid < end - 1 and mid != 0:  # need to store more items in right subtree
            root.right = helper(mid + 1, end)
        return root

    if end is None: end = len(arr)
    return helper(start,end)


class KresgeGrass(Binary_Node):
    def __init__(self, A) -> None:
        '''Initializing the Data Structure from array/list A'''
        self.root = build_subtree(A)

    def get(self,i):
        '''Return the i-th element in your data structure'''
        return self.root.get_node(i)

    def increment(self, a, b, k) -> None:
        '''Increment elements from indices a to b by k'''
        self.root.increment_tree(a,b,k)
