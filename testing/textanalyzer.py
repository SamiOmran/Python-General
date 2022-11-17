def analyze_text(filename):
    """Calculate the number of lines and characters in a file.

    Args:
        filename: The name of the file to analyze.

    Raises:
        IOError: If ``filename`` does not exist or can't be read.

    Returns: The number of lines in the file.
    """
    lines = 0
    characters = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            characters += len(line)
    return lines, characters
