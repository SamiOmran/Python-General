import code
import mmap
import struct
from pprint import pp
from binascii import hexlify


class Vector:

    def __init__(self, mem_float32):
        if mem_float32.format not in "fd":
            raise TypeError('Vector: memoryview values must be '
                            'floating-point numbers')
        if len(mem_float32) < 3:
            raise TypeError('Vector: memoryview must contain at lease 3 floats')
        self._mem = mem_float32

    @property
    def x(self):
        return self._mem[0]

    @property
    def y(self):
        return self._mem[1]

    @property
    def z(self):
        return self._mem[2]

    def __repr__(self):
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)


class Color:

    def __init__(self, mem_uint16):
        if mem_uint16.format not in "HILQ":
            raise TypeError("Color: memoryview values must be unsigned integers")
        if len(mem_uint16) < 3:
            raise TypeError("Color: memoryview must contain at least 3 integers")
        self._mem = mem_uint16

    @property
    def red(self):
        return self._mem[0]

    @property
    def green(self):
        return self._mem[1]

    @property
    def blue(self):
        return self._mem[2]

    def __repr__(self):
        return 'Color({}, {}, {})'.format(self.red, self.green, self.blue)


class Vertex:

    def __init__(self, vector, color):
        self.vector = vector
        self.color = color

    def __repr__(self):
        return 'Vertex({!r}, {!r})'.format(self.vector, self.color)


VERTEX_SIZE = 18
VERTEX_STRIDE = VERTEX_SIZE + 2


def main():
    with open('a.bin', 'rb') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as buffer:
            mem = memoryview(buffer)

            vertex_mems = (mem[i:i + VERTEX_SIZE]
                           for i in range(0, len(mem), VERTEX_STRIDE))

            vertices = [make_colored_vertex(vertex_mem)
                        for vertex_mem in vertex_mems]

            del vertices
            del mem


def make_colored_vertex(mem_vertex):
    mem_vector = mem_vertex[0:12].cast('f')
    mem_color = mem_vertex[12:18].cast('H')

    return Vertex(Vector(mem_vector),
                  Color(mem_color))


if __name__ == '__main__':
    main()
