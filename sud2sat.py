import time

import sys

global output_file
global num_of_clauses
global clause_buffer
global header_buffer


def translate_to_sat(inputfile):
    file = open(inputfile, 'r')

    global num_of_clauses
    num_of_clauses = 0

    global clause_buffer
    clause_buffer = ""
    global header_buffer
    header_buffer = ""

    # Remove new lines in the file
    file = file.read().replace("\r", "").replace("\n", "")

    file_index = 0
    for i in xrange(9):
        line = []
        for j in xrange(9):
            # Read character by character
            c = file[file_index:file_index+1]
            line.append(c)
            # For given numbers, make a rule with them
            if not (c == '0' or c == '.' or c == '?' or c == '*'):
                write_var(i, j, int(c), offsetk=0)
                end_line()
            file_index += 1

    # Add the minimum conditions one by one
    every_cell_has_unique()
    row_uniqueness()
    column_uniqueness()
    grid_uniqueness()

    # Extended conditions
    # one_number_per_entry()
    # once_per_row()
    # once_per_col()
    # once_per_grid()

    # This gets printed first
    header_buffer += "p cnf 729 %s\n" % num_of_clauses


def end_line():
    global clause_buffer
    clause_buffer += "0\n"
    global num_of_clauses
    num_of_clauses += 1


# Each cell can be 1-9
def every_cell_has_unique():
    for i in xrange(9):
        for j in xrange(9):
            for k in xrange(9):
                write_var(i, j, k)
            end_line()


# Each row must have only one of each number
def row_uniqueness():
    for i in xrange(9):
        for k in xrange(9):
            for j in xrange(8):
                # Make rules for a number and the ones after it
                l = j + 1
                while l < 9:
                    write_var(i, j, k, neg=1)
                    write_var(i, l, k, neg=1)
                    end_line()
                    l += 1


# Each column must have only one of each number
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


# brian's additions
def one_number_per_entry():
    for x in range(9):
        for y in range(9):
            for z in range(8):
                i = z + 1
                while i < 9:
                    write_var(x, y, z, neg=1)
                    write_var(x, y, i, neg=1)
                    end_line()
                    i += 1


def once_per_row():
    for y in range(9):
        for z in range(9):
            for x in range(9):
                #sxyz write do we only use neg flag if negation takes place?
                write_var(x, y, z)
            end_line()


def once_per_col():
    for x in range(9):
        for z in range(9):
            for y in range(9):
                #check
                write_var(x, y, z)
            end_line()


def once_per_grid():
    for z in xrange(9):
        for i in xrange(3):
            for j in xrange(3):
                for x in xrange(3):
                    for y in xrange(3):
                        write_var(3 * i + x, 3 * j + y, z)
                end_line()


# Adds a variable to the file buffer, can have negative values. Also has optional offset for k
def write_var(i, j, k, neg=0, offsetk=1):
    global clause_buffer
    if neg == 1:
        clause_buffer += '-'
    if offsetk == 1:
        clause_buffer += str(i * 81 + j * 9 + (k + 1)) + " "
    else:
        clause_buffer += str(i * 81 + j * 9 + k) + " "


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: TOO FEW ARGUMENTS: Please run with \"python sud2sat.py <inputfile> <outputfile>\"")
        exit()

    inputfile = sys.argv[1]
    global output_file
    output_file = open(sys.argv[2], 'w+')

    start = time.time()

    translate_to_sat(inputfile)

    # Print to file
    output_file.write(header_buffer)
    output_file.write(clause_buffer)

    # Print log
    print "Running time: " + str(time.time() - start)
    global num_of_clauses
    print str(num_of_clauses) + " clauses added"
