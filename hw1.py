#!/usr/bin/env python
# ./hw1.py
# Compares the training errors of various features on a given dataset.
#
# By        : Leomar Durán <https://github.com/lduran2/>
# When      : 2021-09-13t22:24
# For       : CIS 4526
# Version   : 1.2
#
# Changelog :
#     v1.2 - 2021-09-13t22:24
#         now counting the rows for the number of samples
#
#     v1.1 - 2021-09-13t21:53
#         reading the names of the features from the CSV files
#
#     v1.0 - 2021-09-13t21:42
#         added argument support, cleaned up the template a bit
#
#     v0.0 - ????-??-??t??:??
#         the tempate

import sys  # for argv
import csv  # for DictReader

def main():
    r'''
    Processes each CSV file passed as an argument.
    '''
    # loop through the arguments (slice off argv[0], the callee)
    for arg in sys.argv[1:]:
        main_arg(arg)
    # end for arg in sys.argv[1:]
# end def main()

def main_arg(arg):
    r'''
    Processes a single CSV file.
    '''
    # open the CSV file
    with open(arg) as csvfile:
        # initialize number of examples at 0
        num_examples = 0

        # Read input file and save attribute names
        # place a dictionary reader on it
        reader = csv.DictReader(csvfile)
        # read in the first row of fields
        attr_names = reader.fieldnames
        # get the number of features
        num_attr = len(attr_names)

        # initialize favorable examples at 0
        attr_train_favorable = [0] * num_attr

        # find number of favorable outcomes
        for row in reader:
            # count this row
            num_examples = (num_examples + 1)
            # print(row)
        # end for row in reader

        # Compute accuracy for each feature
        attr_train_err = [(fav/(num_examples + 1)) for fav in attr_train_favorable]
    # end with open(arg) as csvfile

    # Print out the results
    for attr, err in zip(attr_names, attr_train_err):
        print("Attribute: {}, Training Error: {}".format(attr, round(err, 2)))
    # end for attr, err in zip(attr_names, attr_train_err):
# def main_arg(arg)

if (__name__ == "__main__"):
    main()
