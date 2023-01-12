#Calculate the votes for the candidates in election_data.csv
#Import useful libraries
import os
import csv

from collections import Counter
from csv import DictReader

#Set the path
dir1="."
dir2="Resources"
source_file="election_data.csv"

main_file= os.path.join(dir1,dir2,source_file)

#Initialize variables
Candidate=[]
rowp=[]
total_count =0
candidate_count=0
i=1

#Read the file
with open(main_file, "r") as main:

    #Instead of deleting the first row we read the file as a dictionary. 
    file_reader=DictReader(main)

    #Create a list with the candidates names
    for row in file_reader:
        Candidate.append(row["Candidate"])
        total_count +=1

    #Count the ocurrences of each candidate (i.e. their votes)    
    candidate_count= Counter(Candidate)
    
    #sort by alphabetical order
    candidate_count1=sorted(candidate_count.items())

    #Get the rows to print and save
    rowp.append("Election Results")
    rowp.append("----------------------")
    rowp.append(f"Total votes: {total_count}")
    rowp.append("----------------------")
         
    #loop for printing inidvidual results with asked format
    for politician, votes in candidate_count1:   

        percentage=round(votes/total_count*100,3)
        rowp.append("{} : ({}) ".format(politician,votes)+  str(percentage) +"%")
        
    rowp.append("----------------------")        
    
    #Select the candidate with the most votes
    for politician, votes in candidate_count.most_common():
        if i==1:
            rowp.append(f"Winner: {politician}")
            i +=1
        
#PDisplay the results in terminal
for  row in rowp:             
        print(f"{row}\n")

#Name a file for the output data
dir2="Analysis"
file_name="OutPoll.txt"    

#Create and open a txt file for the results 
new_file=os.path.join(dir1,dir2,file_name)

#Fill the file
with open (new_file,"w" ) as out_file: 
    
    #write analyisis results on the txt file
    for element in rowp:
        out_file.write(element)
        out_file.write("\n")
