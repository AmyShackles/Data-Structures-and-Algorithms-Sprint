Add your answers to the questions below.

1.  What is the runtime complexity of your `depth_first_for_each` method?

    The runtime complexity of my depth_first_for_each is O(n) because it is dependent on the amount of input and every element has to be interacted with once.

2.  What is the space complexity of your `depth_first_for_each` function?

    I would think the space complexity for depth_first_for_each would be O(1) because you're only really looking at one item at a time and not necessarily storing it (because you don't need to know its value beyond what that means in terms of if you take the left or right branch)

3.  What is the runtime complexity of your `breadth_first_for_each` method?

    I would think the runtime complexity for breadth_first_for_each would also be O(n).

4.  What is the space complexity of your `breadth_first_for_each` method?

    Definitely O(n) because you need to keep track of things with the queue in order to have access to neighboring nodes.

5.  What is the runtime complexity of your `heapsort` function?
    For heapsort, I'd think the runtime complexity would be between O(log n) and O(n) because a lot of the work is already done for you in terms of the fact that the heap rearranges itself to fit its own rules.

6.  What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?

    Any time you're making a new array, I think you're getting into the territory of O(n) or greater. It's definitely not constant.

    If it altered the input array, it would probably be O(1) because it's not adding any more space than the original input takes up.
