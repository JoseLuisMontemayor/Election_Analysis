# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes



# Direct Path to file (This works)
# Assign a variable for the file to load the path
file_to_load = "Resources/election_results.csv"

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis
    print(election_data)

# Close the file.
election_data.close()


# Indirect Path to file 

import csv
import os

# Assign a variable for the file  to load and the path. 
file_to_load = os.path.join("Resources","election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Print the file object 
    print(election_data)


#3.4.3 - How to write text to a file
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")

#Close the file
outfile.close()
