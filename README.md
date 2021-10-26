# figshare_geoscrape
Python code for scraping the figshare database and creating an SQLite database of geochemical analyses

Instructions for web scraping code
INSTALLATION
1. Ensure you have the current version of python installed (this code was written in Python 3). Download and install python: https://www.python.org/downloads/
IMPORTANT:
Make sure to add Python as a Path to your computer’s environment. This is usually a check-box in the installation process. Some info on this is here https://datatofish.com/add-python-to-windows-path/ 

2. Get a Figshare API Personal Token: https://help.figshare.com/article/how-to-get-a-personal-token 
There is a place to input your personal token as the top of the scrape script. The token is the security authorisation to access the figshare website and the code will not work without it

3. The database created by this code is and SQL database written in Python using the open source SQLite software. Download and install SQLite: https://www.sqlite.org/download.html 

4. Additional Python libraries that must be installed are sqlite3 and swaggerpy. These can be installed in the command window if a Python path has been added. To use pip install, ensure to change directory in your command window to your local python location, usually: C:\Users\UserName\AppData\Local\Programs\Python\Python39 for example.

Install sqlite3 for python: https://pypi.org/project/db-sqlite3/ 
Install swaggerpy for python: https://pypi.org/project/swaggerpy/ 

OPERATION
1. Unzip the code and save the scripts in a master folder. Copy and paste the 2 scripts (figshare_search.py and databaser.py) and the swagger_client folder into the folder you want to work from.

2. Run the figshare_search.py code first. Follow the steps (1-3) within the code.

3. Next run the databaser.py code. Follow steps 1-3 within the code.

4. After running these two scripts, you will have a set of downloaded supplementary files labelled by the figshare article number and file download ID. These are also stored in the sqlite database you created in the figshare_search.py script. 

5. Clean the data to ensure the column headers are consistent across all files. See Martin et al. (2021) for guidelines. Save the data files as csv files with UTF-8 encoding

6. Run the data_to_sql_database.py code. Follow the instructions within the code to build on the database from Martin et al. (2021) or to create your own new database.

DATA AVAILABILITY:

SQLite template files and metadata available from Figshare: https://doi.org/10.6084/m9.figshare.16870603.v1

To continue to build on the database published by Martin et al. (2021), download the complete Martin et al. database from GEOROC and save as zircon_data.csv, then import the csv into an SQLite Database (first row as headers) and save the database as geoscrape.sqlite in the same folder as the code. 
Download the fsdownload.sqlite file from Figshare: https://doi.org/10.6084/m9.figshare.16870603.v1, and save it into the same folder as the code and the geoscrape.sqlite file.

