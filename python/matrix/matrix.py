'''
Given a string representing a matrix of numbers, return the rows and columns
of that matrix.

So given a string with embedded newlines like:
9 8 7
5 3 2
6 6 7

representing this matrix:
    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7

your code should be able to spit out:
A list of the rows, reading each row left-to-right while moving top-to-bottom
across the rows,
A list of the columns, reading each column top-to-bottom while moving from
left-to-right.

The rows for our example matrix:
9, 8, 7
5, 3, 2
6, 6, 7

And its columns:
9, 5, 6
8, 3, 6
7, 2, 7
'''

class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string 
        
        # Convert matrix string separated by newlines, to a list of lists
        self.matrix_list = [s.split(' ') for s in self.matrix_string.split('\n')]
        
        # Convert every string list from the list to int
        self.matrix_list = [[int(ele) for ele in s] for s in self.matrix_list]

    def row(self, index):
        return self.matrix_list[index-1]

    def column(self, index):
        # For index of every list within the list, return the element
        return [s[index-1] for s in self.matrix_list]