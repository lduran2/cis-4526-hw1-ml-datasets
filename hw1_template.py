def main():
	# Read input file and save attribute names
    attr_names = ["apple", "banana", "carrot"]
    num_attr = 3

    # Compute accuracy for each feature
    attr_train_err = [30.0223, 12.2, 1.1]

    # Print out the results
    for attr, err in zip(attr_names, attr_train_err):
        print("Attribute: {}, Training Error: {}".format(attr, round(err, 2)))

if __name__ == "__main__":
    main()