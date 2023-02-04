# Sudoku
This is an implementation of the `solveSudoku` recursive function. Input any Sudoku board (some of them are in `Sudoku_board.txt`) and see the result of final board.<br><br>
`Zero's` are an empty square.<br><br>

Example input: 

```
000678912
072195348
198342567
859761423
426853791
713924856
961537284
287419035
305286109
```
Output:
```
[
   [5, 3, 4, 6, 7, 8, 9, 1, 2],
   [6, 7, 2, 1, 9, 5, 3, 4, 8],
   [1, 9, 8, 3, 4, 2, 5, 6, 7],
   [8, 5, 9, 7, 6, 1, 4, 2, 3],
   [4, 2, 6, 8, 5, 3, 7, 9, 1],
   [7, 1, 3, 9, 2, 4, 8, 5, 6],
   [9, 6, 1, 5, 3, 7, 2, 8, 4],
   [2, 8, 7, 4, 1, 9, 6, 3, 5],
   [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
```
