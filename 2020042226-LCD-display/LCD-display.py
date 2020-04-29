###############################################################
#
# Author : ELINGUI Pascal Uriel
# Context : Facebook Developer Circle Abidjan Code challenge
# Date : 2020/04/28
# @elinguiuriel
#
###############################################################

# Let us make a bijection from {0, 1, ..., 9} to a special base
# suited to binary operations on LCD numbers
DIGITS = [
    0b1110111,  # 0
    0b0010010,  # 1
    0b1011101,  # 2
    0b1011011,  # 3
    0b0111010,  # 4
    0b1101011,  # 5
    0b1101111,  # 6
    0b1011010,  # 7
    0b1111111,  # 8
    0b1111011,  # 9
]

# DIGITS = [119, 18, 93, 91, 58, 107, 111, 90, 127, 123]


def get_numbers():
    """A function to get numbers as user inputs

    Returns:
        list -- a list of tuples [(s1, n1), (s2, n2), ...]
    """
    numbers = []
    while True:
        # Let us get user input
        line = input()
        if "0 0" in line:
            break

        s, n = line.split()
        numbers.append((s, n))
    return numbers


def display_line(s, n, pointer):
    """Helper function to display a line of an LCD suite of number

    Arguments:
        s {int} -- the size of the block
        n {string} -- the string representation of the number
        pointer {int} -- a pointer used to make binary operations
    """
    for i, c in list(enumerate(n)):
        if DIGITS[int(c)] & pointer:
            print(" " + "-"*s + " ", end="")
        else:
            print(" " * (s+2), end="")
        if i != (len(n)-1):
            print(" ", end="")
    print('')


def display_columns(s, n, pointer):
    """Helper function to display columns of an LCD suite of number

    Arguments:
        s {int} -- the size of the block
        n {string} -- the string representation of the number
        pointer {int} -- a pointer used to make binary operations
    """
    pointer0 = pointer << 1
    count = s
    while count > 0:
        for i, c in list(enumerate(n)):
            if DIGITS[int(c)] & pointer0:
                print("|" + " "*s, end="")
            else:
                print(" "*(s+1), end="")

            if DIGITS[int(c)] & pointer:
                print("|", end="")
            else:
                print(" ", end="")
            if i != (len(n)-1):
                print(" ", end="")
        count -= 1
        print('')


def display(numbers):
    """Format the output

    Arguments:
        numbers {list} - - all the numbers and their size
    """
    for s, n in numbers:
        s = int(s)
        pointer = 0b10000000
        # pointer = 128
        for i in range(5):
            if not i % 2:
                pointer >>= 1
                display_line(s, n, pointer)
            else:
                pointer >>= 2
                display_columns(s, n, pointer)
        print("")


def main():
    """The main function where the logic is combined"""
    numbers = get_numbers()
    display(numbers)


if __name__ == "__main__":
    main()
