'''
Michael Maquera
Calculate Windchill
CS 5001
Fall 2002


windchill.py
'''

from temperature import convert_fahrenheit_to_celsius
from temperature import convert_celsius_to_fahrenheit


def calculate_windchill(temp,speed):
    
    '''
    Windchill Index = (13.12 + 0.6215*T) – (11.37**V0.16) + (0.3965*T*V**0.16)

    V = 1 kilometers per hour = 1.60 mile per hour

    temp_result = temperature in celsius

    '''
    #call the convert function from the temp.py file
    temp_result = convert_fahrenheit_to_celsius( temp )
    #convert mph to kph
    speed_result = speed * 1.60
    
    #calculate the wind chill to celsius
    cel_windchill = 13.12 + (0.6215 * temp_result) - (11.37 * (speed_result ** 0.16)) + (0.3965 * temp_result * (speed_result ** 0.16))
    
    #convert celsius windchill back to fahrenheit
    fah_windchill = convert_celsius_to_fahrenheit(cel_windchill)

    windchill_result = round(fah_windchill,2)

    
    return windchill_result














    
