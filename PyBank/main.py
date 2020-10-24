# -*- coding: utf-8 -*-
#Main script for PyBank written in spyder (python 3.8)
"""
Created on Wed Oct 21 18:05:51 2020

@author: Logan
 
"""
#*****************************************************************************
#importing Dependencies
import csv
#*****************************************************************************
#Declare the file
raw_Data="C:\\Users\\Logan\\Desktop\\bootcamp\\Python-challenge\\python-challenge\\PyBank\\Resources\\budget_data.csv"

#*****************************************************************************
#Empty lists declared
t_Profit = []
months = []
avg_Change = []  
 
#*****************************************************************************       
#Opening/read csv file
with open(raw_Data, newline='', encoding="utf-8") as bd_File:
        csvreader = csv.reader(bd_File, delimiter= ",")
        csvheader = next(bd_File)
        
#*****************************************************************************
#reading in each row of data skipping header               
        for r in csvreader:
            months.append(r[0])
            t_Profit.append(int(r[1]))
            
#*****************************************************************************
# finding average change 
        for x in range(1, len(t_Profit)):
            avg_Change.append((int(t_Profit[x]) - int(t_Profit[x-1])))

#*****************************************************************************
# Calculations            
        t_Avg = sum(avg_Change)/len(avg_Change)
        t_Months =  len(months)
        max_Increase = max(avg_Change)
        max_Month = months[avg_Change.index(max(avg_Change))+1]
        max_Decrease = min(avg_Change)
        min_Month = months[avg_Change.index(min(avg_Change))+1]
        
        
#*****************************************************************************
#Print statements for each section        
        print(f'Finacial Analysis')
        print(f'------------------------------------------')
        print(f'Total Months: \t    {t_Months}')
        print(f'Total: \t\t\t $ {sum(avg_Change)}')
        print(f'Average Change:  $ {round(float(t_Avg),2)}')
        print(f'Greatest Increase in Profit: {max_Month} $ {max_Increase}')
        print(f'Greatest Decrease in Profit: {min_Month} $ {max_Decrease} ')
#*****************************************************************************        
#Printing to file 
output_File="C:\\Users\\Logan\\Desktop\\bootcamp\\Python-challenge\\python-challenge\\PyBank\\Resources\\Financial_Analysis.csv"

with open(output_File,"w") as file:
    
    file.write(f'Finacial Analysis \n')
    file.write(f'------------------------------------------\n')
    file.write(f'Total Months: {t_Months} \n')
    file.write(f'Total: $ {sum(avg_Change)} \n')
    file.write(f'Average Change:  $ {round(float(t_Avg),2)} \n')
    file.write(f'Greatest Increase in Profit: {max_Month} $ {max_Increase} \n')
    file.write(f'Greatest Decrease in Profit: {min_Month} $ {max_Decrease} \n')
    

        