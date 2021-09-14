#!/usr/bin/env python
# ./hw1.py
# Compares the training errors of various features on a given dataset.
#
# By        : Leomar Durán <https://github.com/lduran2/>
# When      : 2021-09-13t21:53
# For       : CIS 4526
# Version   : 1.1
#
# Changelog :
#     v1.0 - 2021-09-13t21:53
#         reading the CSV files, got the names of the features
#
#     v1.0 - 2021-09-13t21:42
#         added argument support, cleaned up the template a bit
#
#     v0.0 - ????-??-??t??:??
#         the tempate

import sys  # for argv
import csv  # for DictReader

def main():
    # loop through the arguments (slice off argv[0], the callee)
    for arg in sys.argv[1:]:
        main_arg(arg)
    # end for arg in sys.argv[1:]
# end def main()

def main_arg(arg):
    # Read input file and save attribute names
    with open(arg) as csvfile:
        reader = csv.DictReader(csvfile)
        attr_names = reader.fieldnames
        num_attr = len(attr_names)

    # Compute accuracy for each feature
    attr_train_err = [30.0223] * num_attr

    # Print out the results
    for attr, err in zip(attr_names, attr_train_err):
        print("Attribute: {}, Training Error: {}".format(attr, round(err, 2)))

if (__name__ == "__main__"):
    main()
