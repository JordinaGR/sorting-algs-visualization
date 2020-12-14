# Sorting and searching algorithms visualization

Vid showing how it works 22/07/2020 version: https://youtu.be/yMG3x2RfGrk

Vid showing how it works 13/09/2020 version: https://youtu.be/ahkvwWWYBDU 	(with merge sort)


Sorting and searching algorithms visualization with python 3.8 and tkinter. The graphics are pretty bad I know, the purpose of this is the algorithm implementation.

There is a timer and the data gets stored in MySQL database. So, I can compare between algorithms doing some statistics. There are two tables, the sorting and the serching algs.

The main file is the sort_alg.py. The algs are in the algs folder. 

The pre folder contains files with programs that creates arrays. They get stored in the 'pre_something' variable (the pre15 contains 15 numbers, the pre30 30 numbers) so you can compare the timing with the same array but different algorithms.

The file sort_algs_noDB.py is the same as the sort_algs.py but without a database, so you can run it on almost all the machines.

The file sort_alg_menu.py is the same but without a database and with the menu in a different window.

#### The sorting algorithms currently implemented are:
- Bubble sort
- Optimized bubble sort
- Selection sort
- Insertion sort
- Quick sort
- Merge sort
- Random sort

#### The searching algorithms currently implemented are:
- Linear search
- Binary search

###### To do list:
- ~~Create a separate menu window in another file~~
- Be able to change speed and create the Entry on sort_alg_noDB
- Add keyboard shortcuts for the menu


Thanks for checking it out.