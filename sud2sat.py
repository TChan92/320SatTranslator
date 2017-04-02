import time

output = open("CNF_Files/1.in", 'w')
global clauses
global file_clauses
global file_header


def main():
    file = open("SudokuPuzzles/sudoku5.txt", 'r')

    puzzle = []
    empty_count = 0
    global clauses
    clauses = 0

    global file_clauses
    file_clauses = ""
    global file_header
    file_header = ""

    for i in xrange(9):
        line = []
        for j in xrange(9):
            c = file.read(1)
            if c == '\r' or c == '\n':
                continue
            line.append(c)
            if c == '0' or c == '.':
                empty_count += 1
            else:
                write_var(i, j, int(c), offsetk=0)
                end_line()
        puzzle.append(line)

    print "unary constraints: " + str(file_clauses.count('\n'))
    every_cell_has_unique()
    print "nineary constraints: " + str(file_clauses.count('\n'))
    every_cell_has_single()
    print "single constraints: " + str(file_clauses.count('\n'))
    row_uniqueness()
    print "row constraints: " + str(file_clauses.count('\n'))
    column_uniqueness()
    print "column constraints: " + str(file_clauses.count('\n'))


    grid_uniqueness()

    file_header += "p cnf 729 %s\n" % clauses


def end_line():
    global file_clauses
    file_clauses += "0\n"
    global clauses
    clauses += 1


def every_cell_has_unique():
    for i in xrange(9):
        for j in xrange(9):
            for k in xrange(9):
                write_var(i, j, k)
            end_line()


def every_cell_has_single():
    for i in xrange(9):
        for j in xrange(9):
            for k in xrange(9):
                l = k + 1
                while l < 9:
                    write_var(i, j, k, neg=1)
                    write_var(i, j, l, neg=1)
                    end_line()
                    l += 1

def row_uniqueness():
    for i in xrange(9):
        for k in xrange(9):
            for j in xrange(8):
                l = j + 1
                while l < 9:
                    write_var(i, j, k, neg=1)
                    write_var(i, l, k, neg=1)
                    end_line()
                    l += 1


def column_uniqueness():
    for j in xrange(9):
        for k in xrange(9):
            for i in range(8):
                l = i + 1
                while l < 9:
                    write_var(i, j, k, neg=1)
                    write_var(l, j, k, neg=1)
                    end_line()
                    l += 1


# This might need additional debugging later since some of these start at 0 and some don't
def grid_uniqueness():
    for z in xrange(9):
        for i in xrange(3):
            for j in xrange(3):
                for x in xrange(3):
                    for y in xrange(3):
                        k = y + 1
                        # This might be n < 4, not sure yet
                        while k < 3:
                            write_var(3 * i + x, 3 * j + y, z, neg=1)
                            write_var(3 * i + x, 3 * j + k, z, neg=1)
                            end_line()
                            k += 1
    for z in xrange(9):
        for i in xrange(3):
            for j in xrange(3):
                for x in xrange(3):
                    for y in xrange(3):
                        k = x + 1
                        while k < 3:
                            for l in xrange(3):
                                write_var(3 * i + x, 3 * j + y, z, neg=1)
                                write_var(3 * i + k, 3 * j + l, z, neg=1)
                                end_line()
                            k += 1


def write_var(i, j, k, neg=0, offsetk=1):
    global file_clauses
    if neg == 1:
        file_clauses += '-'
    if offsetk == 1:
        file_clauses += str(i * 81 + j * 9 + (k + 1)) + " "
    else:
        file_clauses += str(i * 81 + j * 9 + k) + " "



if __name__ == "__main__":
    start = time.time()
    main()
    output.write(file_header)
    output.write(file_clauses)
    print "Running time: " + str(time.time() - start)
    global clauses
    print clauses
