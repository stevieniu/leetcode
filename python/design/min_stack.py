"""
155. https://leetcode.com/problems/min-stack/description/

Design a stack_queue that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack_queue object.
void push(int val) pushes the element val onto the stack_queue.
void pop() removes the element on the top of the stack_queue.
int top() gets the top element of the stack_queue.
int getMin() retrieves the minimum element in the stack_queue.
You must implement a solution with O(1) time complexity for each function.



Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""


class MinStack:

    def __init__(self):
        self.numbers = []
        self.curr_mins = []

    def push(self, val: int) -> None:
        self.numbers.append(val)
        if self.curr_mins:
            cur_min = self.curr_mins[-1]
            self.curr_mins.append(min(cur_min, val))
        else:
            self.curr_mins.append(val)

    def pop(self) -> None:
        self.numbers.pop()
        self.curr_mins.pop()

    def top(self) -> int:
        return self.numbers[-1]

    def getMin(self) -> int:
        return self.curr_mins[-1]

    # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()