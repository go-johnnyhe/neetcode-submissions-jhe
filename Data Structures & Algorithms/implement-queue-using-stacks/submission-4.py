# [1,2,3,4,5]


# queue [2,3,4,5]
# process_stack [5,4,3,2]
# result_stack [6]
class MyQueue:

    def __init__(self):
        self.result_stack = []
        self.process_stack = []

    def push(self, x: int) -> None:
        self.result_stack.append(x)

    def pop(self) -> int:
        length = len(self.result_stack)
        if not self.process_stack:
            while self.result_stack:
                self.process_stack.append(self.result_stack.pop())
        result = self.process_stack.pop()
        return result


    def peek(self) -> int:
        if self.process_stack:
            return self.process_stack[-1]
        else:
            return self.result_stack[0]

    def empty(self) -> bool:
        return True if len(self.result_stack) == 0 and len(self.process_stack) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()