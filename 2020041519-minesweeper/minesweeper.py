###############################################################
#
# Author : ELINGUI Pascal Uriel
# Context : Facebook Developer Circle Abidjan Code challenge
# Date : 2020/04/19
# @elinguiuriel
#
###############################################################


def get_fields():
    """A function to get fields as user inputs"""
    fields = {}
    id = 1
    while True:
        # first let us get the field dimensions
        line = input()
        if "0" in line:
            break

        n, m = line.split()
        n, m = int(n), int(m)

        # Now let us fill the field
        field = []
        for i in range(n):
            l = input().split()[:m]
            if len(l) != m:
                raise Exception("Invalid number of items a line {}".format(i))
            field.append(l)

        fields[id] = field
        id += 1

    return fields


def get_adjacent_cells(mat, point):
    """Get the coordonates of all the adjacent cells for a given point
    in a matrix

    Arguments:
        mat {tuple} -- the dimension of the matrix in tuple (n, m)
        point {tuple} -- the coordonate (x, y) of the point

    Returns:
        list -- a list of tuples [(x1, y1), (x2, y2), ...]
    """
    adjacents = []
    offsets = (0, 1, -1)
    for i in offsets:
        for j in offsets:
            if i == 0 and j == 0:
                continue
            x, y = (point[0]+i, point[1]+j)
            if x < 0 or y < 0 or x >= mat[0] or y >= mat[1]:
                continue
            adjacents.append((x, y))

    return adjacents


def gen_weighted_fields(fields):
    """Get the weighted fields from the inputed one

    Arguments:
        fields {dict} -- the input fields

    Returns:
        weighted_fields {dict} -- the weighted_fields
    """
    weighted_fields = {}

    for id in range(len(fields)):
        field = fields[id+1]
        weighted_fields[id+1] = []
        n = len(field)
        m = len(field[0])
        for i in range(n):
            row = []
            for j in range(m):
                if field[i][j] == '*':
                    row.append('*')
                else:
                    adjacents = get_adjacent_cells((n, m), (i, j))
                    weight = sum([field[x][y] == '*' for x, y in adjacents])
                    row.append(weight)
            weighted_fields[id+1].append(row)

    return weighted_fields


def display(weighted_fields):
    """Format the output

    Arguments:
        weighted_fields {dict} -- all the weighted fields
    """
    for id in range(len(weighted_fields)):
        print("Champ #{}".format(id+1))
        field = weighted_fields[id+1]
        for i in range(len(field)):
            print(' '.join([str(val) for val in field[i]]))
        print('\n')


def main():
    """The main function where the logic is combined"""
    fields = get_fields()
    weighted_fields = gen_weighted_fields(fields)
    display(weighted_fields)


if __name__ == "__main__":
    main()
