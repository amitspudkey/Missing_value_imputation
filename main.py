import pandas as pd
from file_handling import *
from selection import *

print("Program: Missing value imputation")
print("Release: 0.1.0")
print("Date: 2020-03-26")
print("Author: Brian Neely")
print()
print()
print("The program reads a csv file and imputes a custom value, mean, min, max, or median for missing values.")
print()
print()


def imputation(data):
    # Column list
    headers = list(data.columns)

    # Perform missing value imputation on all columns or select columns
    run_options = ['Use all columns', 'Select certain columns', 'Cancel and close']
    selected_run_option = list_selection(run_options, 'Select column selection type', 'selection type')

    # Column Selection for selecting certain columns
    if selected_run_option == 'Select certain columns':
        # Select Columns for missing data imputation
        columns = column_selection_multi(headers, 'missing value imputation')
    elif selected_run_option == 'Use all columns':
        # Use all columns
        columns = headers
    else:
        # Cancel and return original dataset
        print()
        return data

    # Ask what to impute data with
    imputation_type = ['Custom Value', 'Column Mean', 'Column Max', 'Column Min', 'Column Median', 'Cancel and close']
    selected_imputation_type = list_selection(imputation_type, 'Select imputation policy', 'imputation using')

    # Impute missing values
    if selected_imputation_type == 'Custom Value':
        imputed_value = input('Enter value for imputation: ')
        print("Performing imputation...")
        data[columns] = data[columns].fillna()
        print("Imputation Done!")
    elif selected_imputation_type == 'Column Mean':
        print("Performing imputation...")
        data[columns] = data[columns].fillna(data.mean())
        print("Imputation Done!")
    elif selected_imputation_type == 'Column Max':
        print("Performing imputation...")
        data[columns] = data[columns].fillna(data.max())
        print("Imputation Done!")
    elif selected_imputation_type == 'Column Min':
        print("Performing imputation...")
        data[columns] = data[columns].fillna(data.min())
        print("Imputation Done!")
    elif selected_imputation_type == 'Column Median':
        print("Performing imputation...")
        data[columns] = data[columns].fillna(data.median())
        print("Imputation Done!")
    else:
        print('An error has occurred. Program closing...')

    # Return dataset
    return data


# Set input file
file_in = select_file_in()

# Ask for delimination
delimination = input("Enter Deliminator: ")

# Set output file
file_out = select_file_out_csv(file_in)

# Import data
data = open_unknown_csv(file_in, delimination)
print()

# Run imputation function
data = imputation(data)

# Run additional imputation
additional_imputation = y_n_question('Run another imputation (y/n): ')
while additional_imputation:
    data = imputation(data)
    additional_imputation = y_n_question('Run another imputation (y/n): ')

# Output dataset
data.to_csv(file_out, index=False)
