"""Class to demonstrate how iterators work"""


class ExampleIterator:
    def __init__(self):
        self.index = 0
        self.data = [1, 2, 3]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()
        result = self.data[self.index]
        self.index += 1
        return result


class AlternateIterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __getitem__(self, idx):
        return self.data[idx]

l = [i for i in AlternateIterable()]
print(l)
