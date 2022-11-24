# Write a Python program find a list of integers with exactly
# two occurrences of nineteen and at least three occurrences of five


# list = [19, 19, 15, 5, 3, 5, 5, 2]


def check(list):
    return list.count(19) == 2 and list.count(5) >= 3


class Test:
    def __init__(self):
        print('this is a test initializer')


def student_data(stu_id, *args, **kwargs):
    print('regular argument ', stu_id)
    print('positional argument ', args)
    print('keyword argument ', kwargs)


class Vector:

    def __init__(self, **coords):
        private_coords = {'_' + k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __getattr__(self, name):
        private_name = '_' + name
        try:
            return self.__dict__[private_name]
        except KeyError as e:
            raise AttributeError('{!r} object has no attribute {!r}'.format(
                type(self).__name__, name))

    def __setattr__(self, name, value):
        raise AttributeError('Cannot set attribute {!r}'.format(name, value))

    def __repr__(self):
        return "{}({})".format(
            type(self).__name__,
            ', '.join("{k}={v}".format(
                k=k[1:],
                v=self.__dict__[k])
                for k in sorted(self.__dict__.keys())))


"""python
    from practice import *
    v=Vector(x=1,y=2) 
ddas"""