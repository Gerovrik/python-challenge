# -*- coding: utf-8 -*-
#Main script for PyPoll
"""
Created on Wed Oct 21 18:07:14 2020

@author: Logan
"""
#*****************************************************************************
#importing Dependencie
import csv

#*****************************************************************************
#Declare the file
raw_Data="C:\\Users\\Logan\\Desktop\\bootcamp\\Python-challenge\\python-challenge\\PyPoll\\Resources\\election_data.csv"

#*****************************************************************************
#Variables initialized
t_Votes = 0; Khan_votes = 0; Correy_votes = 0; Li_votes = 0; Otooley_votes = 0

#*****************************************************************************
#Opening/read csv file

with open(raw_Data, newline="", encoding = "utf-8") as Votes:
    
    csv_Reader = csv.reader(Votes,delimiter = ",")
    
    header = next(csv_Reader)
#*****************************************************************************
#Setting up For loop to put csv into lists
    for i in csv_Reader:
        
        voter_Id =   i[0]
        county =     i[1]
        candidate =  i[2]
        
        # Total votes iteration and addition
        t_Votes +=1 
        
        #ifelse statement for counting votes of each candidate
        if candidate == "Khan":
            Khan_votes +=1 
        elif candidate == "Correy":
            Correy_votes +=1 
        elif candidate == "Li":
            Li_votes +=1 
        elif candidate == "O'Tooley":
            Otooley_votes +=1 
            
#*****************************************************************************
#Creating a dictionary then finding Max votes to get winner
Who = ["Khan", "Correy", "Li", "O'Tooley"]
p_V = [Khan_votes, Correy_votes, Li_votes, Otooley_votes]
candidate_Outcome=  dict(zip(Who, p_V))
winner = max(candidate_Outcome,  key=candidate_Outcome.get)

#*****************************************************************************
#Doing math for Percent of total votes for each candidate
Kahn_p =        (Khan_votes / t_Votes)*100
Correy_p =      (Correy_votes / t_Votes)*100
Li_p =          (Li_votes / t_Votes)*100
Otooley_p =     (Otooley_votes / t_Votes)*100

#*****************************************************************************
#print out statements for each results
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {t_Votes}')
print(f'-------------------------')
print(f'Kahn: {Kahn_p:.3}% {Khan_votes}')
print(f'Correy: {Correy_p:.3}% {Correy_votes}')
print(f'Li: {Li_p:.3}% {Li_votes}')
print(f'OTooley: {Otooley_p:.3}% {Otooley_votes}')
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')
#*****************************************************************************
#creating output file using With open to write to file
output_File="C:\\Users\\Logan\\Desktop\\bootcamp\\Python-challenge\\python-challenge\\PyBank\\Resources\\Poll_Results.csv"

with open(output_File,"w") as file:
    
    file.write(f'Election Results')
    file.write(f'-------------------------')
    file.write(f'Total Votes: {t_Votes}')
    file.write(f'-------------------------')
    file.write(f'Kahn: {Kahn_p:.3}% {Khan_votes}')
    file.write(f'Correy: {Correy_p:.3}% {Correy_votes}')
    file.write(f'Li: {Li_p:.3}% {Li_votes}')
    file.write(f'OTooley: {Otooley_p:.3}% {Otooley_votes}')
    file.write(f'-------------------------')
    file.write(f'Winner: {winner}')
    file.write(f'-------------------------')
     


