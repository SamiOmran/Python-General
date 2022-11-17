"""Read and print an integer series."""

import sys


def read_series(filename):
    try:
        series = []
        recaman = open(filename, mode='r', encoding='utf-8')
        series = [int(line.strip()) for line in recaman]
    except(ValueError, IOError) as e:
        print("{0}".format(e))
    finally:
        recaman.close()

    return series


def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main(sys.argv[1])
