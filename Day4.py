
test_grid = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

with open("day4.txt", "r") as f:
    actual_grid = f.read()

def grid_to_matrix(grid:str)->[[str]]:
    # whereas the boundaries are "."
    matrix = [list(row) for row in grid.split()]
    matrix.insert(0, ["." for _ in range(len(matrix[0]))])
    for r in matrix:
        r.insert(0, ".")
        r.append(".")
    matrix.append(["." for _ in range(len(matrix[0]))])
    return matrix

recurr = 0
def find_all_rolls(matrix:[[str]]):
    accessible_rows = 0
    marked_matrix = [row.copy() for row in matrix]
    # A simple matrix.copy or matrix[:], wouldn't work here
    # because the list(list) the rows are still passed by reference


    for m in range(1, len(matrix[0]) - 1): # minus one because of the boundaries
        for n in range(1, len(matrix) - 1):
            neighbours = []
            if matrix[m][n] == "@":
                # upper three
                neighbours += [matrix[m - 1][n + i] for i in range(-1, 2)]
                neighbours += [matrix[m][n + i] for i in range(-1, 2)]
                neighbours += [matrix[m+1][n + i] for i in range(-1, 2)]
                if neighbours.count("@") - 1 < 4:
                    # print(neighbours, neighbours.count("@"))
                    accessible_rows += 1
                    marked_matrix[m][n] = "X"

    for row in marked_matrix:
        print(row)

    # Part ONE return:
    # return accessible_rows

    # Part Two recursive return:
    # global recurr
    # recurr += 1
    # print(recurr) # 72 recursions for the actual grid
    if accessible_rows == 0: return 0
    return accessible_rows + find_all_rolls(marked_matrix)


print(find_all_rolls(grid_to_matrix(actual_grid)))
