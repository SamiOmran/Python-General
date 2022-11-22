"""A module for demonstrating exceptions."""
import sys


def convert(s):
    """Convert to an integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        #print("Failed to convert with exception {0}".format(str(e)), file=sys.stderr)
        print("Payload", e.args)
        return -1


def main():
    print(convert('3s'))


if __name__ == "__main__":
    main()
