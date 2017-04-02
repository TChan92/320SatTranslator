output = open("CNF_Files/1.in", 'w')

def main():
    file = open("SudokuPuzzles/1.txt", 'r')

    puzzle = []
    empty_count = 0

    output.write("c Sudoku number 1\n")
    output.write("p cnf 729 \n")

    for i in xrange(9):
        line = []
        for j in xrange(9):
            c = file.read(1)
            line.append(c)
            if c == '0':
                empty_count += 1
        puzzle.append(line)

    every_cell_has_number()

    row_uniqueness()

    column_uniqueness()

    


def every_cell_has_number():
    for i in xrange(9):
        for j in xrange(9):
            for k in xrange(9):
                write_var(i, j, k)
            output.write("0\n")


def row_uniqueness():
    for i in xrange(9):
        for j in xrange(9):
            for k in xrange(8):
                l = k + 1
                while l < 9:
                    write_var(i, j, k, neg=1)
                    write_var(i, j, l, neg=1)


def column_uniqueness():
    for i in xrange(9):
        for j in xrange(9):
            for k in range(8):
                l = k + 1
                while l < 9:
                    write_var(j, i, k, neg=1)
                    write_var(j, i, l, neg=1)


def write_var(i, j, k, neg=0):
    if neg == 1:
        output.write('-')
    output.write(str(i * 81 + j * 9 + (k + 1)) + " ")


if __name__ == "__main__":
    main()