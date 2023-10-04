# Open the file
f = open("films.dat")
# For each line, strip the newline character and add the line to the list
lines = [line.rstrip() for line in f.readlines()]
# Close the file
f.close()

# Create an empty dictionary to store the data
media = {}

for line in lines:
    # for each line, split the line at the colon and store the film name and year in a list
    x = line.split(": ")
    # Add the film name as the key and the year as the value to the dictionary
    media[x[0]] = x[1]

# Print the dictionary
print(media)
