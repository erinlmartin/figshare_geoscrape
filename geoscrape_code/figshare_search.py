'''

@author: ErinMartin

This code searches the figshare database for articles, compiles them in a list
then extracts downloadable files and metadata from the list and inputs it into
an sqlite database

'''
#%%

# STEP 1: Enter data and execute this section of the code

#   Enter the search term below as a string, i.e. within " "
searchterm = " "

#   Set the maximum number of results to collect (integer, maximum 999)
limit = 

#   Enter your figshare API token below (as a string)
TOKEN = " "

#   Enter the filename for the sqlite database in which to store your metadata. 
#   If you have not yet created a database, enter a new filename and the 
#   database will be created. Input is a string that must end in .sqlite
#   To build on the database from Martin et al. (2021) (Download from: )
#   enter "fsdownloads.sqlite". To use the template file enter "fsdownloads_template.sqlite".
#   Download SQLite files from: https://doi.org/10.6084/m9.figshare.16870603.v1
sqlite_filename = " .sqlite"

#   Add any terms to be excluded from the search (these will be marked irrelevant and not downloaded)
#   Enter the terms to be excluded between the ' ' and separate each term by a comma

excludedterms =['','']

#%%

# STEP 2: Execute this block of code to define the function

def figshare_search(searchterm, limit, TOKEN, sqlite_filename):
        
    import swagger_client 
    from swagger_client.rest import ApiException
    import urllib.request, urllib.parse, urllib.error
    import sqlite3
    import json
    
    apilist = list()
    url = 'https://api.figshare.com/v2/articles'
    # urllib.request.urlretrieve(url)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    # Configure OAuth2 access token for authorization: figshare_oauth
    swagger_client.configuration.access_token = TOKEN
    
    # create an instance of the API class
    api_instance = swagger_client.ArticlesApi()
    # enter search term here
    search =  {
    "search_for": searchterm,
    "limit": limit
    }
    
    try: 
        # Public Articles Search
        global api_response
        api_response = api_instance.articles_search(search=search)
        #pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArticlesApi->articlesSearch: %s\n" % e)
        
    type(api_response)
    print(len(api_response))
    #print(item.__dict__)
    
    apilist.clear()
    
    for item in api_response:
        address = item.url
        apilist.append(address)
        
    print("apilist length =", len(apilist))
    
    
    conn = sqlite3.connect(sqlite_filename)
    cur = conn.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS article
        (article_id INTEGER PRIMARY KEY
            AUTOINCREMENT,
         articlenum TEXT UNIQUE, 
         title TEXT UNIQUE, 
         citation TEXT UNIQUE,
         paper_doi TEXT, 
         paper_title TEXT, 
         license TEXT,
         author TEXT,
         funding TEXT,
         relevance TEXT)''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS doitable
        (doi_id  INTEGER PRIMARY KEY
            AUTOINCREMENT, 
         doi TEXT UNIQUE,
         article_id INTEGER)''')
        
    cur.execute('''CREATE TABLE IF NOT EXISTS description
        (description_id  INTEGER PRIMARY KEY
            AUTOINCREMENT, 
         descrip TEXT UNIQUE,
         article_id INTEGER)''')    
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Files 
        (downloadurl_id INTEGER PRIMARY KEY,
         article_id INTEGER, 
         file_type TEXT, 
         download_url TEXT,
         status TEXT)''')
        
    cur.execute('''CREATE TABLE IF NOT EXISTS authors 
        (author_id INTEGER PRIMARY KEY
            AUTOINCREMENT,
        article_id	INTEGER,
		author_name	TEXT, 
        orcid_id TEXT UNIQUE)''')
    
    ent = 1
    for entry in apilist:
        url = entry
        print("Entry", ent)
        print('Accessing api site', url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print('Accessed', len(data), 'characters')
        ent = ent+1
    
        info = json.loads(data)
    
    
        articlenumber = info['id']
        title = info['title']
        citation = info['citation']
        dois = info['doi']
        description = info['description']
        paper_doi = info['resource_doi']
        paper_title = info['resource_title']
        lic = info['license']['name']
        auth = info['authors'][0]['full_name']
        fund = info['funding']
        status = "unretrieved"
        relevance = "relevant"
        irrelevant = "irrelevant"
    
    
        print((articlenumber, title))
        
        try:
            cur.execute('''INSERT OR IGNORE INTO article
                    (articlenum, 
                     title, 
                     citation, paper_doi, paper_title, license, author, funding, relevance)
                    VALUES ( ?, ?, ?, ?, ?, ?,?,?, ?)''', ( articlenumber, title, citation, paper_doi, paper_title, lic, auth, fund, relevance))
            cur.execute('SELECT article_id FROM article WHERE articlenum = ? ', (articlenumber,  ))
            article_id = cur.fetchone()[0]
        
            cur.execute('''INSERT OR IGNORE INTO doitable (doi, article_id)
                        VALUES ( ?, ? )''', ( dois, article_id, ))
            cur.execute('SELECT doi_id FROM doitable WHERE doi = ? ', (dois, ))
            doitable_id = cur.fetchone()[0]
            
            cur.execute('''INSERT OR IGNORE INTO description (descrip, article_id)
                        VALUES ( ?, ? )''', ( description, article_id, ))
            cur.execute('SELECT description_id FROM description WHERE descrip = ? ', (description, ))
            description_id = cur.fetchone()[0]
            conn.commit()
            
            for f in info['files']:
              file_type = f['name']
              download_url = f['download_url']
              cur.execute('''INSERT OR IGNORE INTO Files
                          (article_id, 
                           file_type, 
                           download_url, status) 
                          VALUES ( ?, ?, ?, ? )''',
              (article_id, file_type, download_url, status))
              cur.execute('SELECT downloadurl_id FROM files WHERE download_url = ? ', (download_url, ))
              downloadurl_id = cur.fetchone()[0]
              conn.commit()
              
            for a in info['authors']:
              author_name = a['full_name']
              orcid_id = a['orcid_id']
              cur.execute('''INSERT OR IGNORE INTO authors
                          (article_id, 
                           author_name, 
                           orcid_id) 
                          VALUES ( ?, ?, ? )''',
              (article_id, author_name, orcid_id))
              cur.execute('SELECT author_id FROM authors WHERE author_name = ? ', (author_name, ))
              author_id = cur.fetchone()[0]
              conn.commit()  
        except: continue
    
        for i in excludedterms:
            cur.execute(''' UPDATE article
                        SET relevance=?
                        WHERE article.citation LIKE ?''',
           (irrelevant, i,))
   
       # if ent == limit+1: break
         
     
    conn.commit()
        
    conn.close()
    
#%%

# STEP 3: Execute the function calling the variables assigned in STEP 1.
# Those variables can be modified and STEP 3 repeated without executing STEP 2.

figshare_search(searchterm, limit, TOKEN, sqlite_filename)    
    
