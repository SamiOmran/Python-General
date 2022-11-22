class Base:
    def __init__(self):
        print('Base initializer')

    def f(self):
        print('Base.f()')


class Sub(Base):
    def __init__(self):
        print('Sub initializer')

    def f(self):
        print('Sub.f()')


class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)


class SortedList(SimpleList):
    def __init__(self, items=()):
        print('SortedList initializer')
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))


class IntList(SimpleList):
    def __init__(self, items=()):
        print('IntList initializer')
        for x in items:
            self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values')

    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "IntList({!r})".format(list(self))


"""Multiple inheritance"""
class SortedIntList(IntList, SortedList):
    pass

    # def __repr__(self):
    #     return 'SortedIntList({!r})'.format(list(self))


class A:
    def func(self):
        return 'A.func'


class B(A):
    def func(self):
        return 'B.func'


class C(A):
    def func(self):
        return 'C.func'

        
class D(B, C):
    pass


# if __name__ == '__main__':
    # simple_list = SimpleList([1, 4, 65654, 2])
    # simple_list.sort()
    # print(simple_list)
    # b = Base()
    # s = Sub()
    # s.f()
