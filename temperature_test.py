'''
    Michael Maquera
   CS5001
   Fall 2020
   Homework 2: Temperature Converter test code
'''

from temperature import convert_celsius_to_fahrenheit
from temperature import convert_fahrenheit_to_celsius

def test_temp_converter(input_c,expected_f,input_f,expected_c):

    result_f= convert_celsius_to_fahrenheit( input_c )
    result_c=  convert_fahrenheit_to_celsius( input_f )
    print('Celcius test result: {:.2f}, expected: {:.2f}'.format(result_c, expected_c))
    print( 'Fahrenheit test result: {:.2f}, expected: {:.2f}'.format(result_f, expected_f))    


def main():
    '''
    test cases:
    celcius to fahrenheit input: 30  , expected 86
    fahrenheit to celcius input: 100  , expected 38

    test_temp_converter(input_c, expected_F, input_f, expected_C)
    
    '''
    
    test_temp_converter( 30, 86 , 100, 38 )
    
    

main()
