"""A module for dealing with BMP bitmap image files."""


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.
    Args:
        filename: The name of the BMP file to be created.
        pixels: A rectangular image stored as a sequence of rows.
            Each row must be an iterable series of integers in the
            range 0-255.
    Raises:
        OSError: If the file couldn't be written.8
    """

    length = len(pixels)
    width = len(pixels[0])

    with open('files/img.bmp', 'wb') as bmp:
        bmp.write(b'BM')
        size = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00')
        bmp.write(b'\x00\x00')
