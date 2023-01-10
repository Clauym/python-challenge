#BUDGET ANALYSIS FOR BANK
# Initializing variables
tot_month=int(0)
sum_pl=0
change=float(0)
cont=int(0)

avg_chg=float(0)
grt_inc=[]
grt_dec=[]
Dates=[]
pl_chg=[0]
row_b=[]

import csv
import os 

#Defining source file path    

dir0='.'
dir1='Resources'
file_name='budget_data.csv'

#Create the route to the input file
main_file=os.path.join(dir0,dir1,file_name)

#Open the file to read. 
with open (main_file,"r") as src_file:

    #Check for the variables in the source    
    tot_line=csv.reader(src_file, delimiter= ",")
    #Drop out the header
    header = next(tot_line)
    
    #Calculate the sum of montly PL 
    for lines in tot_line:
        tot_month+=1
        sum_pl=int(lines[1])+sum_pl

        #Create a list for the dates that will serve as reference 
        Dates.append(lines[0])
       
       #trick to avoid a mistake in the first monthly difference
        if cont==0:
            pl_past=int(lines[1])
            cont+=1
        else:
            pl_new=int(lines[1])
            #Calculate the monthly change of PL
            change=pl_new - pl_past
            pl_past=pl_new
            #Fill the list with PL values
            pl_chg.append(change)

    #Find max and min of the monthly Pl changes
    grt_inc=max(pl_chg)
    grt_dec=min(pl_chg)
    
    #Look for the corresponding dates for the max and min in the Date string
    F_maxi=Dates[pl_chg.index(grt_inc)]
    F_maxd=Dates[pl_chg.index(grt_dec)]
    
    #Calculate the Avergae PL change
    avg_chg=sum(pl_chg)/ (tot_month-1)
    
    #Calculate the date for date stamp
    from datetime import date 
    now = date.today( )

    #Set the data to be printed
    row_b.append("Financial Analysis")
    row_b.append("--------------")
    row_b.append(f"Total Months: {tot_month}")
    row_b.append(f"Total: ${sum_pl}")
    row_b.append(f"Average change: ${round(avg_chg,2)}")
    row_b.append(f"Greatest Increase in Profits: {F_maxi}  (${grt_inc})")
    row_b.append(f"Greatest Decrease in Profits: {F_maxd} (${grt_dec})")
    row_b.append('---')
    row_b.append(f"Data calculated as of {now}")

    #Display the analysis output at the terminal
    for element in row_b:
        print(element)
    
#Name a file for the output data
dir1="Analysis"
file_name="OutputBank.txt"
    

#Create and open a txt file for the results 
new_file=os.path.join(dir0,dir1,file_name)
with open (new_file,"w" ) as out_file: #Res_file:
    
    #write analyisis results on the txt file
    for element in row_b:
        wr_line=element.split(",")
        out_file.write(element)
        out_file.write("\n")
 