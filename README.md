# SatTranslator
## Authors
Tim Chan (V00803066), Moad Ben-Suleiman (V00807282), Brian McCormack (V00818130)

## Run Instructions
sud2sat.py takes a sudoku file and turns it into a DIMACs format file for use with a SAT solver, specifically minisat.
It can be run with the command 
```{r, engine='bash', count_lines}
python sud2sat.py <inputfile> <outputfile>
```
where inputfile is a sudoku file and outputfile is the output file for the sud2sat

<br>
sat2sud.py takes a minisat output file and translates it into a readable sudoku file. It can be run with the command 
```{r, engine='bash', count_lines}
python sat2sud.py <inputfile> <outputfile>
```
where <inputfile> is the output of minisat and <outputfile> is the output for sat2sud

<br>
testing.sh can be run to help test. It run the 50 files inside SudokuPuzzles and give the solved puzzles inside CNF_Out


## Included Files
|File Name|Description|
|---------|------------|
|Documentation.txt   |  Contains instructions on how to use files |
|sud2sat.py         | Changes file to DIMANCS format for use with a sat solver|
|sat2sud.py         | Changes file from SAT output to readable format|
|testing.sh         | Runs through all the puzzles in SudokuPuzzles puts the output into CNF_Out|
|testingHard.sh     | Runs through all the hard puzzles in HardPuzzles and puts the output into CNF_Hard_Files|

## Bonus Features
Hard Puzzles are solvable using this program because they are parsed into individual files.

The extended encoding is also completed and it can be acccessed by uncommenting
lines 45-49 in sud2sat.py
