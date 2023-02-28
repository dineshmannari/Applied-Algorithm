#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv
# import pandas as pd

col=[]
# Open the CSV file using the 'with' statement
with open('D:/MS sem2/DM/homework 4/archive/nyt-comments-2020.csv', 'r') as csv_file:
    
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Iterate over the rows in the CSV file
    for row in csv_reader:
        col1 = row[1]
        col2 = row[7]
        col.append([col1,col2])
#         print(column1, column2)
dataobj = pd.DataFrame(col, col=['commentBody', 'Status'])

# Print the DataFrame
print(dataobj.head)


# In[ ]:




