#!/usr/bin/env python
# ./hw1.py
# Compares the training errors of various features on a given dataset.
#
# By        : Leomar Durán <https://github.com/lduran2/>
# When      : 2021-09-13t21:42
# For       : CIS 4526
# Version   : 1.5
#
# Changelog :
#     v1.0 - 2021-09-13t21:42
#         added argument support, cleaned up the template a bit
#
#     v0.0 - ????-??-??t??:??
#         the tempate

import sys

def main():
    # loop through the arguments (slice off argv[0], the callee)
    for arg in sys.argv[1:]:
        main_arg(arg)
    # end for arg in sys.argv[1:]
# end def main()

def main_arg(arg):
    # Read input file and save attribute names
    attr_names = ["apple", "banana", "carrot"]
    num_attr = 3

    # Compute accuracy for each feature
    attr_train_err = [30.0223, 12.2, 1.1]

    # Print out the results
    for attr, err in zip(attr_names, attr_train_err):
        print("Attribute: {}, Training Error: {}".format(attr, round(err, 2)))

if (__name__ == "__main__"):
    main()
