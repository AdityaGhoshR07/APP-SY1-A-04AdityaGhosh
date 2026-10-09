#Create a script to read data from an input file. Perform count lines, extract first two lines
#and write the extracted data into a new file.
input_file = open("input.txt","r")
lines= input_file.readlines()
input_file.close()

line_count = len(lines)
first_two_lines=lines[:2]

output_file=open("output.txt","w")
output_file.writelines(first_two_lines)
output_file.close()

print(f"Total number of lines: {line_count}")
print("Extracted lines written to output.txt")