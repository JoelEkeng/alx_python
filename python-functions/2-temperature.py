#!/usr/bin/env python3

#convert_to_celsius = __import__('2-temperature').convert_to_celsius

def convert_to_celsius(fahrenheit):
    Celsius = (fahrenheit - 32) * (5/9)
    if Celsius % 4 == 0:
        if Celsius == 0:
            return "{:.1f}".format(Celsius)
        else:    
            return "{:.0f}".format(Celsius)
    if fahrenheit < 0:
        return "{:.2f}".format(Celsius)
    else:
        return Celsius
