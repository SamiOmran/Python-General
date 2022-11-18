"""__main__ module to run the directory directly, without specifying the module name"""
import sys

segments = sys.argv[1:]
text = ' '.join(segments)
output = ('words = {0}, chars = {1}'.format(len(text.split()), sum(len(w) for w in text.split())))

print(output)
