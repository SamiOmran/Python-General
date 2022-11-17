from itertools import count, islice

"""learn how to deal with files in python"""

file_one = open('files/wasteland.txt', mode='wt', encoding='utf-8')

file_one.write('I am writing to the file some text.\nsaxsass')
file_one.write('eeee')

file_one.write(' nice')
file_one.write(' really?')

file_one.close()

file_one = open('files/wasteland.txt', mode='rt', encoding='utf-8')

print(file_one.read())


def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence():
    """Write Recaman's sequence to a text file."""
    with open('files/Recaman.dat', mode='wt', encoding='utf-8') as f:
        f.writelines("{0}\n".format(r)
                     for r in islice(sequence(), 9))


def count_words_per_line(file):
    with open(file, mode='rt', encoding='utf-8') as f:
        return [len(line.split()) for line in f]


print(count_words_per_line('files/wasteland.txt'))

write_sequence()


def count_lines(filename):
    with open(filename, mode='rt', encoding='utf') as f:
        print(len(f.read()))


count_lines('files/wasteland.txt')
