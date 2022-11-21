def colors(red, blue, **kwargs):
    print(red, blue, kwargs)


# colors('red', 'blue', color='green')


def print_args1(arg1, arg2, arg3, *args):
    print(arg1, arg2, arg3, args)


t = (1, 2, 3, 4, 5, 6, 6)


# print_args1(*t)
# print_args1(1, 2, 3, 'hello')


def print_args2(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


# print_args2(t[0], t[1], kwarg1=t[2], kwarg2=t[3])


def sort_by_last_letter(strings):
    def last_letter(str):
        return str[-1]

    return sorted(strings, key=last_letter)


strings = ['hello', 'from', 'a', 'local', 'function']
# print(sort_by_last_letter(strings))

# print(strings)
# strings = sorted(strings, key=lambda str: str[-1])


g = 'global'


def outer(p='param'):
    l = 'local'

    def inner():
        print('inside inner')
        print(g, p, l)

    print('before inner function')
    inner()


# outer()


def enclosing():
    str = 'hello'
    def local_func():
        print(str)

    return local_func

l = enclosing()

print(l.__closure__)
