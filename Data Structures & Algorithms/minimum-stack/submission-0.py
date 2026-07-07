class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_num = 0
        if len(self.stack) > 0:
            min_num = 9999999999999
            
        for s in self.stack:
            if s < min_num:
                min_num = s
        
        return min_num