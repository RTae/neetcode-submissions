class Deque:
    
    def __init__(self):
        self.q = []

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def append(self, value: int) -> None:
        self.q.append(value)

    def appendleft(self, value: int) -> None:
        self.q = [value] + self.q

    def pop(self) -> int:
        if len(self.q) == 0:
            return -1
        
        return self.q.pop(-1)

    def popleft(self) -> int:
        if len(self.q) == 0:
            return -1

        return self.q.pop(0)
