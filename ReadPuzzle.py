import re

puzzles_file = open("50Puzzles.txt", 'r')

for i in xrange(1,51):
    puzzles_file.readline()
    dest = open("SudokuPuzzles/" + str(i) + ".txt", 'w')
    numread = 0
    while numread < 9 * 9:
        c = puzzles_file.read(1)
        if c == '\n':
            continue
        if c == '.' or c == '*' or c == '?':
            dest.write('0')
        else:
            dest.write(c)
        numread += 1
    puzzles_file.read(1)