#!/usr/bin/env python
# ./hw1.py
# Compares the training errors of various features on a given dataset.
#
# By        : Leomar Durán <https://github.com/lduran2/>
# When      : 2021-09-13t23:29
# For       : CIS 4526
# Version   : 1.3
#
# Changelog :
#     v1.3 - 2021-09-13t23:29
#         uses the first row as a control row for non-numerical data
#
#     v1.2.3 - 2021-09-13t23:11
#         calculating the average rate of failure as error properly
#
#     v1.2.2 - 2021-09-13t22:34
#         calculating probability for each feature as error
#
#     v1.2.1 - 2021-09-13t22:24
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
        # Read input file and save attribute names
        # place a dictionary reader on it
        reader = csv.DictReader(csvfile)
        # read in the first row of fields
        fields = reader.fieldnames
        # dictionaries are ordered in Python 3.6,
        # so we can just slice off the result field
        attr_names = fields[:-1]
        label = fields[-1]
        # get the number of features
        num_attr = len(attr_names)

        # create control using row data 1
        control = next(reader)

        # initialize to 1s because first row as control is all passes
        # absolute error (before dividing by number of examples)
        attr_train_err_abs = [1] * num_attr
        # number of examples
        num_examples = 1

        # find the absolute errors
        for row in reader:
            # count this row
            num_examples = (num_examples + 1)
            # count every absolute error
            for k, name in enumerate(attr_names):
                # does the current feature fail the test?
                bin_feature = (row[name] == control[name])
                bin_label = (row[label] == control[label])
                curr_fail = (bin_feature != bin_label)
                # accumulate the fails
                attr_train_err_abs[k] = (attr_train_err_abs[k] + curr_fail)
            # end for k, name in enumerate(attr_names)
        # end for row in reader

        # Compute accuracy for each feature
        attr_train_err = [(err_abs/num_examples) for err_abs in attr_train_err_abs]
    # end with open(arg) as csvfile

    # Print out the results
    for attr, err in zip(attr_names, attr_train_err):
        print("Attribute: {}, Training Error: {}".format(attr, round(err, 2)))
    # end for attr, err in zip(attr_names, attr_train_err):
# def main_arg(arg)

if (__name__ == "__main__"):
    main()
# end if (__name__ == "__main__")
