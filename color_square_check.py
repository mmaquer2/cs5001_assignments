'''
Michael Maquera
CS 5001
Fall 2020
HW 3
color_sqaure_check
'''

def check_valid_row(row_input):
    if row_input <= 8 and row_input >=1:
        print('row input is valid')
        return True
    else:
        print('im sorry that is not a valid row input')
        return False    

def check_valid_column(col_input):  
    if col_input <= 104 and col_input > 96:
        print('column input is valid')
        return True
    else:
        print('im sorry that is not a valid column input')
        return False
        
    
