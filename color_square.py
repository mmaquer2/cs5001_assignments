'''
Michael Maquera 
CS 5001 HW3
Fall 2020

color_sqaure.py

'''

from color_square_check import check_valid_row
from color_square_check import check_valid_column 


def main():
 print('please choose a position on the grid')
 col_input = str(input('pick a column, a to h  '))
 row_input = int(input('pick a row, 1 to 8  '))
 ##make all column inputs lower case
 col_lower = col_input.lower()
 #get ascii value of the col character
 col = int(ord(col_lower))
 #runs the validation check for column and row inputs
 check_valid_column(col)
 check_valid_row(row_input)

 comparing_value = row_input + col
 #determine the color of the square based on the ascii values
 if(comparing_value % 2 == 0):
     #even ascii values are black grids
     print('block', col_input,row_input, 'is black')
 else:
     #odd ascii values are white grids
     print('block', col_input,row_input, 'is white')
 
main()
 


