SATSOLVER CSC320 By Tim Chan (V00803066), Moad Ben-Suleiman (V00807282), Brian McCormack (V00818130)

Instructions on how to use our programs are in Documentation.txt

Included files:
Documentation.txt   Contains instructions on how to use files
sud2sat.py          Changes file to DIMANCS format for use with a sat solver
sat2sud.py          Changes file from SAT output to readable format
testing.sh          Runs through all the puzzles in SudokuPuzzles puts the output into CNF_Out
testingHard.sh      Runs through all the hard puzzles in HardPuzzles and puts the output into CNF_Hard_Files

Bonus Tasks:
Hard Puzzles are solvable using this program, they were parsed into individual files
The extended encoding is also complete, it can be acccessed by uncommenting
lines 45-49 in sud2sat.py
