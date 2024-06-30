class Solution:
    def __init__(self):
        self.d={}
    def fib(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        else:
            if n<=1:
                return n
            else:
                self.d[n] = self.fib(n-1)+self.fib(n-2)
                return self.d[n]