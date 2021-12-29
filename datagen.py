
import csv 
import numpy as np

fields = ["Roll No","cat 1","cat 2","cat 3","overall","conversion","Result"]

n = 6000

filename = "student.csv"
rows = []



for rollno in range(1,n+1):

    RollNo = rollno
    cat_2 = np.random.randint(10,50)
    cat_3 = np.random.randint(10,50)
    cat_1 = np.random.randint(10,50)
    overall = cat_1 + cat_2 + cat_3
    conversion = int(overall * 100 / 150)

    if(conversion >= 70):
        result = "fast learners"

    elif(conversion >= 50):
        result = "Average learners"
   
    elif(conversion <= 40):
        result = "slow leaners"
    else:
        result = "slow leaners"
    
   
    rows.append([RollNo,cat_1,cat_2,cat_3,overall,conversion,result])


with open(filename, 'w') as csvfile: 

    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)

