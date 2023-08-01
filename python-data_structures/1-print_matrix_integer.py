#!/usr/bin/python

def print_matrix_integer(matrix=[[]]):
    if matrix == " ":
        print()
        return

    for row in matrix:
        for i, elements in enumerate(row):
            print("{:d}".format(elements), end="")

            if i < len(matrix) - 1:
                print(" ", end="")
       
        print()   
