#!/usr/bin/env python3

#fibonacci_sequence = __import__('4-fibonacci').fibonacci_sequence

def fibonacci_sequence(n):
    if (n == 0):
        Sequence_list = []
        return Sequence_list
    elif (n == 1):
        Sequence_list = [0]
        return Sequence_list
    elif (n == 2):
        Sequence_list = [0, 1]
        return Sequence_list

    Sequence = [0, 1]

    for i in range (2, n):
        Fibonacci_sequence = Sequence[-1] + Sequence[-2]
        Sequence.append(Fibonacci_sequence)
        
    return Sequence
    