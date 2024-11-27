class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._cookies = 0
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError("")


    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError("")
        self._cookies += n

    def withdraw(self, n):
        if self._cookies < n:
            raise ValueError("")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

