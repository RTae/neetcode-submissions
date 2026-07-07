class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.length = 0
        self.arr = [0]*self.cap

    def get(self, i: int) -> int:
        if i < self.length:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i >= 0 and i < self.length:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.cap:
            self.resize()

        self.arr[self.length] = n
        self.length+=1

    def popback(self) -> int:
        if self.length != 0:
            self.length-=1
            return self.arr[self.length] 

    def resize(self) -> None:
        self.cap = self.cap*2
        temp = [0]*self.cap

        for i in range(self.length):
            temp[i] = self.arr[i]

        self.arr = temp

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.cap
