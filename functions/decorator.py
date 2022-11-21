
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def print_nablus():
    return'Nablusø'


print(print_nablus())


class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


@CallCount
def hello(name):
    print('Hello {}'.format(name))


tracer = Trace()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


@tracer
@escape_unicode
def nablus_maker(name):
    return name + 'øy'
