# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:25:34 2021

@author: emar0032


CREATES AN SQL DATA TABLE TO STORE WED SCRAPED AND CLEANED DATA


"""
#%%

#   Specify the name of the sqlite database you would like to store your
#   data in. This can be a new data sheet or the existing "zircon_datasheet.sqlite"
#   created by Martin et al. (2021). Ensure the database file is in the same
#   working folder as the files you would like to input into the database.

sqlite_filename = "zircon_datasheet.sqlite"

#   Enter the name of the data table within the SQL database that the data will 
#   be entered into. For example, if using the database from Martin et al. (2021)
#   enter "zircon_data"

sql_datatable = "zircon_data"


#   To create a new SQLite databse from scratch, see instructions at the bottom 
#   of this code
#%%

#   STEP 1
#   Execute this code to connect to the database

import pandas as pd
import sqlite3
import re

file = sqlite_filename
conn = sqlite3.connect(file)
cur = conn.cursor()

print("connection established")

#%%

#   STEP 2
#   Copy the relative path of the file you wish to push to the database and
#   when prompted, paste as the Data file name.
#   Read the list of columns to ensure they match the formatting of the SQLite
#   datatable

# opens the csv file
csv_name = input('Data file name? ')
read = pd.read_csv(csv_name)
df = pd.DataFrame(read)

# extracts article id from filename
prefix = re.findall('^[0-9]+', csv_name)
pre = [str(pref) for pref in prefix]
article_id = "".join(pre)

df.insert(column='article_id', value = article_id, loc=1)       

df.columns

#%%

#   STEP 3
#   Execute this code to push the data to the database
#   Continue to repeat STEP 2 and 3

df.to_sql(sql_datatable, if_exists='append', con=conn, index=False)

conn.commit()   

df.to_csv(csv_name)  

#%%%

#   Close the connection to the database when you are done

conn.close()


#%%
"""
  If an error is thrown relating to a column not existing in the datatable,
  there are three possible solutions:
"""
#%%

#   SOLUTION 1 - Manually add the new column to the datatable in SQLite

#   Open the database in SLQite then select the Database Structure tab, then
#   right click on the table name and select Modify Table. 
#   Manually add the new column and data type and reload the database here

#%%

#   SOLUTION 2 - Drop the unwanted column from the dataframe

#   Add the columns that need to be dropped to the list below using the syntax
#   ['bad_column1',  'bad_column2'], and then execute the code

cols_to_drop = []

df=df.drop(columns = cols_to_drop)

#%%

#   SOLUTION 3 - Correct misspelled column headers

#   Add the misspelled header and the correct spelling to the dictionary below
#   using the syntax   {'incorrect1' : 'correct1', 'incorrect2' : 'correct2'}
#   then execute the code below

misspelled_headers = {}

df.rename(columns = misspelled_headers, inplace=True)

#%%
"""
    Creating a new SQLite database from scratch can be done either within
    Python or in the SQLite GUI
    
    NB: This can also be done by creating a new sql database in SQLite
    and importing a .csv file with headers in the first row
    
"""
#%%

#   To creat the database in python you will need:
#   1. a filename 
#   2. a name for the table thaat wil hold your data
#   3. a list of columns and corresponding datatypes
    

#%%%

#   Enter the filename you have chosen for your database

file = input('Database_file? ')
conn = sqlite3.connect(file)
cur = conn.cursor()

#%%

#   Fill in the SQL code below:
#   Enter the name of your table in the first line, replacing table_name_here   
#   For each subesquent row (except entry_id) enter a column header (no spaces)
#   and a corresponding datatype - either INTEGER, REAL or TEXT. Ensure each
#   row ends with a comma and continue until each column in your data table
#   has been defined. Then execute the code 


cur.execute('''CREATE TABLE IF NOT EXISTS table_name_here
    (entry_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     column2 TEXT , 
     column3 TEXT, 
     column4 TEXT, 
     column5 REAL)''')     
    
#%%

