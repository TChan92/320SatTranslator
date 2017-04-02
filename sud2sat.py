import time

output = open("CNF_Files/1.in", 'w')
global clauses


def main():
    file = open("SudokuPuzzles/1.txt", 'r')

    puzzle = []
    empty_count = 0
    global clauses
    clauses = 0

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

    grid_uniqueness()


def endline():
    output.write("0\n")
    global clauses
    clauses += 1

def every_cell_has_number():
    for i in xrange(9):
        for j in xrange(9):
            for k in xrange(9):
                write_var(i, j, k)
            endline()


def row_uniqueness():
    for i in xrange(9):
        for j in xrange(9):
            for k in xrange(8):
                l = k + 1
                while l < 9:
                    write_var(i, j, k, neg=1)
                    write_var(i, j, l, neg=1)
                    endline()
                    l += 1


def column_uniqueness():
    for i in xrange(9):
        for j in xrange(9):
            for k in range(8):
                l = k + 1
                while l < 9:
                    write_var(j, i, k, neg=1)
                    write_var(j, i, l, neg=1)
                    endline()
                    l += 1


# This might need additional debugging later since some of these start at 0 and some don't
def grid_uniqueness():
    for z in xrange(9):
        for i in xrange(2):
            for j in xrange(2):
                for x in xrange(3):
                    for y in xrange(3):
                        k = y + 1
                        # This might be n < 4, not sure yet
                        while k < 3:
                            write_var(3 * i + x, 3 * j + y, z, neg=1)
                            write_var(3 * i + x, 3 * j + k, z, neg=1)
                            endline()
                            k += 1
    for z in xrange(9):
        for i in xrange(2):
            for j in xrange(2):
                for x in xrange(3):
                    for y in xrange(3):
                        k = y + 1
                        while k < 3:
                            for l in xrange(3):
                                write_var(3 * i + x, 3 * j + y, z, neg=1)
                                write_var(3 * i + k, 3 * j + l, z, neg=1)
                                endline()
                            k += 1


def write_var(i, j, k, neg=0):
    if neg == 1:
        output.write('-')
    output.write(str(i * 81 + j * 9 + (k + 1)) + " ")


if __name__ == "__main__":
    start = time.time()
    main()
    print "Running time: " + str(time.time() - start)
    global clauses
    print clauses
