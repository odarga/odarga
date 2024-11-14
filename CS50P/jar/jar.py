class Jar:
    def __init__(self, capacity = 12, size = 0):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = size

    def __str__(self):
        s = "🍪" * self.size
        return f"{s}"

    def deposit(self, n):
        if self.capacity - n < 0:
            raise ValueError
        self.capacity -= n
        self.size = 12 - self.capacity

    def withdraw(self, n):
        if self.capacity + n > 12:
            raise ValueError
        self.capacity += n
        self.size = 12 - self.capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()
    while True:
        try:
            while True:
                action = input("add or remove? ")
                if action.lower() in ("add", "remove"):
                    break
                else:
                    print("allowed commands: add / remove")

            while True:
                try:
                    cookies = int(input("number of cookies: "))
                except ValueError:
                    pass
                else:
                    if action == "add":
                        jar.deposit(cookies)
                    else:
                        jar.withdraw(cookies)
                    break
        except EOFError:
            print()
            break
        else:
            print("size:", jar.size)
            print("capacity:", jar.capacity)
            print(jar)


if __name__ == "__main__":
    main()
