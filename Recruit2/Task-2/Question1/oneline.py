import csv
# Open the input file for reading
with open('/Users/sanjevr/Documents/GitHub/Cognizance/Recruit2/Task-2/Question1/onelinefile.txt', 'r') as f:
    contents = f.read().strip() # Read the contents of the file and remove any leading/trailing white spaces
# Initialize an empty list to store the data
data = []
# Loop through the contents of the file and split the data based on their format
i = 0
while i < len(contents):
    ID = int(contents[i])
    name = contents[i+1:i+4]
    marks = contents[i+4:i+8]
    subject_end = i + 8 + len(contents[i+8:].split()[0])
    subject = contents[i+8:subject_end]
    data.append((ID, name, marks, subject))
    i = subject_end
    print("\n")
# Open the output CSV file for writing
with open('/Users/sanjevr/Documents/GitHub/Cognizance/Recruit2/Task-2/Question1/Filename2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(['ID', 'Name', 'Marks', 'Subject'])
    # Write the data rows
    for row in data:
        writer.writerow(row)
        print("\n")