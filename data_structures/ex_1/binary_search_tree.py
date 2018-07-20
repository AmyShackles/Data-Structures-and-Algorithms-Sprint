class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        # invoke callback with value of self
        cb(self.value)
        # if there is a left branch,
        # invoke the callback with the left branch
        if self.left:
            self.left.depth_first_for_each(cb)
        # if there is a right branch,
        # invoke the callback with the right branch
        if self.right:
            self.right.depth_first_for_each(cb)

    # # iterative from lecture
    # def depth_first_for_each(self, cb):
    #     stack = []
    #     stack.append(self)

    #     while len(stack):
    #         current_node = stack.pop()
    #         if current_node.right:
    #             stack.append(current_node.right)
    #         if current_node.left:
    #             stack.append(current_node.left)
    #         cb(current_node.value)

    def breadth_first_for_each(self, cb):
        # create a queue
        queue = []
        # add the binary tree to that queue
        queue.append(self)
        # while there are nodes in that queue,
        # remove the first node and return it
        while len(queue) > 0:
            node = queue.pop(0)
            # if that element has a node to its left,
            # add the node to its left to the queue
            if node.left:
                queue.append(node.left)
            # if that node has a node to its right,
            # add the node to its right to the queue
            if node.right:
                queue.append(node.right)
            # invoke the callback with the value of the node
            cb(node.value)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if value < self.value:
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
