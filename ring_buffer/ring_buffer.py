class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_index = 0

    def __repr__(self):
        return "[" + ", ".join([str(i) for i in self.storage]) + "]"

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.oldest_index] = item
            self.oldest_index += 1
            if self.oldest_index == self.capacity:
                self.oldest_index = 0

    def get(self):
        return self.storage
