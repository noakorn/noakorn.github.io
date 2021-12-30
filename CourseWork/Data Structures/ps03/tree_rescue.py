

class Node(object):
    """Even though we are not asking for a tree in return,
    feel free to use this Node class to help you build the tree.
    """

    def __init__(self, key) -> None:
        self.key = key

        self.left = None
        self.right = None

    def __repr__(self):
        l = None if self.left is None else self.left.key
        r = None if self.right is None else self.right.key
        return "[{},{},{}]".format(l,self.key,r)

    def traverse(self):
        left = self.left.traverse() if self.left else []
        right = self.right.traverse() if self.right else []
        return left + [self.key] + right


def tree_rescue(A, L):
    """Rescue the tree from the a list of keys in a specific order and a list of levels
    for each corresponding keys.

    The provided list `A` has a special order as follows,

        ```
        A = []
        def collect_nodes(node):
            if node is None:
                return

            A.append(node)
            collect_nodes(node.left)
            collect_nodes(node.right)
        ```

    Args:
        A (List[int]): List of keys in the order specified above.
        L (List[int]): Level of each of the keys in the same order.

    Returns: (List[int])
        A list of keys in the 'in-order' traversal of the constructed binary-tree.
    """
    def helper(tree,L,curr_level):
        # The first value in A is always the current root of the subtree
        # the base case is when we have one element left in the array
        if tree is None:
            return None
        root = Node(tree[0])
        if len(tree) == 1:
            return root

        # we otherwise proceed to dividing into our two subtrees
        next_level = curr_level + 1

        # look for the indices of the nodes that are in the same level
        indices = [i for i,char in enumerate(L) if char == next_level]

        # There's at least 1 index for the next level and at most 2
        left_subtree = tree[indices[0]:indices[1]] if len(indices) == 2 else tree[indices[0]:]
        left_L = L[indices[0]:indices[1]] if len(indices) == 2 else L[indices[0]:]
        right_subtree = tree[indices[1]:] if len(indices) == 2 else None
        right_L = L[indices[1]:] if len(indices) == 2 else None
        root.left = helper(left_subtree,left_L,next_level)
        root.right = helper(right_subtree,right_L,next_level)
        return root
    return helper(A,L,0).traverse()

