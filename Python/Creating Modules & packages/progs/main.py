import csv

# Input and output file paths
input_file = "C:\\Users\\PTB3KOR\\Documents\\Python\\WQU-Data science lab\\projects\\010-housing-in-mexico\\New Text Document.txt"
output_file = 'C:\\Users\\PTB3KOR\\Documents\\Python\\WQU-Data science lab\\projects\\010-housing-in-mexico\\brasil-real-estate-1.csv'

# Read the data from the input text file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Process the data and split values
data = []
for line in lines:
    # Remove leading/trailing whitespaces and newline characters
    line = line.strip()

    # Split values based on the delimiter '|'
    values = line.split(',')

    # Append the split values to the data list
    data.append(values)

# Write the data to a CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data saved to", output_file)