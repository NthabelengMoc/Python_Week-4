def read_and_write_file(input_file, output_file):
	with open(input_file, 'r') as infile:
		content = infile.read()

	modified_content = content.upper()

	with open(output_file, 'w') as outfile:
		outfile.write(modified_content)

input_file = 'sample.txt'  # Input file
output_file = 'modify.txt'  # Output file
read_and_write_file(input_file, output_file)

print("File has been read and modified content written to", output_file)
