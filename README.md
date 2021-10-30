# Sorting and searching algorithms visualization

Vids showing how it works (DD/MM/YYYY):

1. 22/07/2020 version #1: https://youtu.be/yMG3x2RfGrk

2. 13/09/2020 version #2: https://youtu.be/ahkvwWWYBDU 

3. 16/12/2020 version #3: https://youtu.be/uF0zBXybNJ0

4. 03/02/2021 version #4: https://youtu.be/Nc4NOI1vlrQ

5. 01/08/2021 version #5: https://youtu.be/fRDp73723Z8

Sorting and searching algorithms visualization with python 3.8 and tkinter. The purpose of this is the algorithm implementation.

There is a timer and the data gets stored in MySQL database. So, I can compare between algorithms doing some statistics. There are two tables, the sorting and the serching algs.

The pre folder contains files with programs to create arrays. They get stored in the 'pre_something' variable so you can compare the timing with the same array but different algorithms.

The file sort_algs_noDB.py is the same as the sort_algs.py but without a database, so you can run it on almost all the machines. And is not updated. The sort_alg_clean.py is up to date and where I do all the changes.

The file sort_alg_menu.py is the same but with the menu in a different window and not updated.

There's a new database in .csv files, these files are useded by the sort_alg_clean.py. When you click the button database in the menu, a new window opens with the .csv information. That window is made in other/database_button.py

#### The sorting algorithms currently implemented are:
- Bubble sort
- Optimized bubble sort
- Selection sort
- Insertion sort
- Quick sort
- Merge sort
- Random sort
- Shell sort
- Counting sort
- Radix sort
- Cocktail sort

#### The searching algorithms currently implemented are:
- Linear search
- Binary search
- Exponential search