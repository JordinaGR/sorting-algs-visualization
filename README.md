# Sorting and searching algorithms visualization

Vids showing how it works (DD/MM/YYYY):

1. 22/07/2020 version #1: https://youtu.be/yMG3x2RfGrk

2. 13/09/2020 version #2: https://youtu.be/ahkvwWWYBDU 

3. 16/12/2020 version #3: https://youtu.be/uF0zBXybNJ0


Sorting and searching algorithms visualization with python 3.8 and tkinter. The graphics are pretty bad I know, the purpose of this is the algorithm implementation.

There is a timer and the data gets stored in MySQL database. So, I can compare between algorithms doing some statistics. There are two tables, the sorting and the serching algs.

The pre folder contains files with programs to create arrays. They get stored in the 'pre_something' variable so you can compare the timing with the same array but different algorithms.

The file sort_algs_noDB.py is the same as the sort_algs.py but without a database, so you can run it on almost all the machines. And is not updated. The sort_alg_menu.py is up to date and where I do all the changes.

The file sort_alg_menu.py is the same but without a database, with the menu in a different window and updated.

There's a new database in .csv files, these files are useded by the sort_alg_menu.py. When you click the button database in the menue, a new window opens with the .csv information. That window is made in other/database_button.py


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


###### To do list:
- ~~Create a separate menu window in another file~~
- ~~Be able to change speed and create the Entry on sort_alg_noDB~~
- ~~More options to generate data~~
- ~~Button to save the data and use it later~~
- Rearrange the menu controls
- ~~Shell sort~~
- Button to show database information in a different window
- ~~Radix sort~~
- Bind scroll bar on database table

Thanks for checking it out.