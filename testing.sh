#!/bin/bash
#!/usr/bin/env python
for filename in SudokuPuzzles/*.txt; do
    name=${filename##*/}
    base=${name%.txt}
    python2.7 sud2sat.py "$filename" "CNF_Files/$base.in"
done

for cnf in CNF_Files/*.in; do
    name=${cnf##*/}
    base=${name%.in}
    minisat "$cnf" "CNF_Files/$base.out"
done

for out in CNF_Files/*.out; do
    name=${out##*/}
    base=${name%.out}
    python2.7 sat2sud.py "$out" "CNF_Out/$base.txt"
done