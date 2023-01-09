#BUDGET ANALYSIS FOR BANK
# Initializing variables
Tot_month=int(0)
Sum_PL=0
Change=float(0)
cont=int(0)

Avg_chg=float(0)
Grt_inc=[]
Grt_dec=[]
Dates=[]
PL_chg=[0]
Row=[]

import csv
import os 

#Defining source file path    
dir1="c:\\"
dir2="Users"
dir3="Celvir"
dir4="python-challenge"
dir5="PyBank"
dir6="Resources"
file_name="budget_data.csv"

Main_file=os.path.join(dir1,dir2,dir3,dir4,dir5,dir6,file_name)
print (Main_file)
#os.path.normpath(Main_file)

#print(Main_file)
#Open the file to read. Did't specify if it ws just readable 
#    due to the command messing with the route

with open (Main_file) as Src_File:

    #Check for the variables in the source    
    Tot_line= csv.reader(Src_File, delimiter= ",")
    #Drop out the header
    header = next(Tot_line)
    
    #Calculate the sum of montly PL 
    for lines in Tot_line:
        Tot_month+=1
        Sum_PL=int(lines[1])+Sum_PL

        #Create a list for the dates that will serve as reference 
        Dates.append(lines[0])
       
       #trick to avoid a mistake in the first monthly difference
        if cont==0:
            PL_past=int(lines[1])
            cont+=1
        else:
            PL_new=int(lines[1])
            #Calculate the monthly change of PL
            Change=PL_new - PL_past
            PL_past=PL_new
            #Fill the list with PL values
            PL_chg.append(Change)

    #Find max and min of the monthly Pl changes
    Grt_inc=max(PL_chg)
    Grt_dec=min(PL_chg)
    
    #Look for the corresponding dates for the max and min in the Date string
    F_maxi=Dates[PL_chg.index(Grt_inc)]
    F_maxd=Dates[PL_chg.index(Grt_dec)]
    
    #Calculate the Avergae PL change
    Avg_chg=sum(PL_chg)/ (Tot_month-1)
    
    #Calculate the date for date stamp
    from datetime import date 
    now = date.today( )

    #Set the data to be printed
    Row.append("Financial Analysis")
    Row.append("--------------")
    Row.append(f"Total Months: {Tot_month}")
    Row.append(f"Total: ${Sum_PL}")
    Row.append(f"Average Change: ${round(Avg_chg,2)}")
    Row.append(f"Greatest Increase in Profits: {F_maxi}  (${Grt_inc})")
    Row.append(f"Greatest Decrease in Profits: {F_maxd} (${Grt_dec})")
    Row.append('---')
    Row.append(f"Data calculated as of {now}")

    #Display the analysis output at the terminal
    for element in Row:
        print(element)
    
#Name a file for the output data
dir6="Analysis"
file_name="OutputBank.txt"
    

#Create and open a txt file for the results 
New_file=os.path.join(dir1,dir2,dir3,dir4,dir5,dir6,file_name)
with open (New_file,"w" ) as Out_file: #Res_file:
    
    #write analyisis results on the txt file
    for element in Row:
        wr_line=element.split(",")
        Out_file.write(element)
        Out_file.write("\n")
 