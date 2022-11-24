""""""


def is_comment(item):
    return isinstance(item, str) and item.startswith('#')


def execute(program):
    """Execute a stack program.

    Args:
        program: Any stack-like collection where each item in the stack
            is a callable operator or non-callable operand. The top-most
            items on the stack may be strings beginning with '#' for
            the purposes of documentation.  Stack-like means support for:

                item = stack.pop()  # Remove and return the top item
                stack.append(item)  # Push an item to the top
                if stack:           # False in a boolean context when empty
    """
    # Find the start of the 'program' by skipping
    # any item which is a comment.
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else:  # nobreak
        print("Empty program!")
        return

    # Evaluate the program
    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print("Error: ", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:  # nobreak
        print("Program successful.")
        print("Result: ", pending)

    print("Finished")


# if __name__ == '__main__':
#     import operator
#
#     program = list(reversed((
#         "# A short stack program to add",
#         "# and multiply some constants",
#         9,
#         13,
#         operator.mul,
#         2,
#         operator.add)))
#
#     execute(program)

# def match(i):
#     return i == 66
#
#
# iterable = [2,45,66,3]
# for item in iterable:
#     if match(item):
#         result = item
#         break
# else:  # nobreak
#     # No match found
#     print('did not enter')
#     result = None
#
# # Always come here
# print(result)


items = [2, 25, 9, 37, 28, 14]
divisor = 12

for item in items:
    if item % divisor == 0:
        found = item
        break
else:  # nobreak
    items.append(divisor)
    found = divisor

print("{items} contains {found} which is a multiple of {divisor}"
      .format(**locals()))
