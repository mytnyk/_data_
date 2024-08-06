import os
import csv
import re

def read_custom_format(filename):
    with open(filename, 'r') as file:
        # Read the first part (input features)
        num_observations_input, num_features_input = map(int, file.readline().strip().split())
        input_features = []
        for _ in range(num_observations_input):
            input_features.append(file.readline().strip().split())

        # Read the second part (output features)
        num_observations_output, num_features_output = map(int, file.readline().strip().split())
        output_features = []
        for _ in range(num_observations_output):
            output_features.append(file.readline().strip().split())

        # Read the third part (description of the dataset)
        while file.readline().strip() != "#Variables:":
            pass
        input_feature_names_line = file.readline().strip()
        output_feature_names_line = file.readline().strip()
        input_feature_names = re.split(r'\s*,\s*|\s+', input_feature_names_line)
        output_feature_names = re.split(r'\s*,\s*|\s+', output_feature_names_line)

    return input_features, output_features, input_feature_names, output_feature_names

def write_to_csv(input_features, output_features, input_feature_names, output_feature_names, output_filename):
    with open(output_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write header
        header = input_feature_names + output_feature_names
        csvwriter.writerow(header)

        # Write data
        for input_row, output_row in zip(input_features, output_features):
            csvwriter.writerow(input_row + output_row)

def convert_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".iom"):
            input_filepath = os.path.join(directory, filename)
            output_filepath = os.path.join(directory, f"{os.path.splitext(filename)[0]}.csv")
            
            input_features, output_features, input_feature_names, output_feature_names = read_custom_format(input_filepath)
            write_to_csv(input_features, output_features, input_feature_names, output_feature_names, output_filepath)
            print(f"Converted {input_filepath} to {output_filepath}")

def main():
    directory = input("Enter the directory path: ")
    convert_files_in_directory(directory)

if __name__ == "__main__":
    main()
