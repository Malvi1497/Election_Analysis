# add dependancies
import csv
import os

# Assign a variable to to load a file from our path
file_to_load = os.path.join("Resources" , "election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("analysis" , "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
     # To do analysis with the data
     # To print each row in the csv file
     # for row in file_reader:
          # print(row)
# To print first item from each row
# for row in file_reader:
     # print(row[0])
# To print the header row
     # Read the file object with the reader function
     file_reader = csv.reader(election_data)
     headers = next(file_reader)
     print(headers) 

