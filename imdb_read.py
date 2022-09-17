'''Original Copyright to Erina Kim'''

''' Reference to IMDB Sentiment Analysis Dataset
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}'''

''' Reference to Opinion Lexicon
Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews."
Proceedings of the ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, Washington, USA,
Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing
and Comparing Opinions on the Web." Proceedings of the 14th
International World Wide Web conference (WWW-2005), May 10-14, 2005, Chiba, Japan.'''

# Import pyodbc, pandas, numpy, nltk, sqlite libraries
import pyodbc
import sqlalchemy
import sqlite3
from sqlalchemy import create_engine
import pandas as pd
pd.options.display.max_rows = 60000

import numpy as py
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

import warnings
warnings.filterwarnings("ignore")

# Open IMDB Dataset with 50,000 Reviews
imdb = pd.read_csv('C:/Erina/SQL Practice/IMDB Dataset.csv', encoding='latin1')

# Tokenize each review using NLTK
# Launch RegexpTokenizer to reduce the errors due to unspaced words after punctuation
tokenizer = RegexpTokenizer(r'\w+')
token_list = imdb['review'].map(tokenizer.tokenize)

# Create the DataFrame to store our analysis data
df = pd.DataFrame()

# Import existing information from the IMDB dataset to our dataframe
df['Review ID'] = imdb['ID']
df['Review'] = imdb['review']

# Open positive and negative word dataset composed of 2005 and 4796 words each
positive = open('C:/Erina/SQL Practice/positive-words.txt', encoding='latin1').read()
negative = open('C:/Erina/SQL Practice/negative-words.txt', encoding='latin1').read()

positive_word = word_tokenize(positive)
negative_word = word_tokenize(negative)

# Create the List for 3 criteria: First singular pronoun, Word Tone, Word Count
pronoun = ['i','my', 'me', 'mine','myself']
tone = list()
pronoun_match = list()
count_list = list()

# Set up the default value for list as 0
ps_count = 0
ng_count = 0
pronoun_count = 0

# Use For Loop to count matching criteria in each token
for idx in token_list:
    count_list.append(len(idx))
    for token in idx:
        
        if token.lower() in pronoun:
            pronoun_count += 1

        if token in positive_word:
            ps_count += 1
        elif token in negative_word:
            ng_count += 1
    
    # Add the calculated value from each token to 3 criteria list
    pronoun_match.append(pronoun_count)

    # Word Tone:
    # positive if tokens in each reivew are matching more with words from positive data
    # negative if tokens in each reivew are matching more with words from negative data
    # neutral if numbers are same or not matching with any word from the given dataset
    if ps_count > ng_count:
        tone.append("positive")
    elif ps_count < ng_count:
        tone.append("negative")
    else:
        tone.append("neutral")

    # Reset the count values for next index
    ps_count = 0
    ng_count = 0
    pronoun_count = 0

# Assign 3 criteria list to our dataframe
df['Number of Words'] = count_list
df['Number of First Pronoun'] = pronoun_match
df['Word Tone'] = tone

# Also add the original sentiment analysis to our dataframe to compare
df['Rating'] = imdb['sentiment']

# Create a SQLite database with engine
#engine = create_engine('sqlite:///C:\\Erina\\SQL Practice\\imdb_database.db?charset=utf8', echo = False)
#df.to_sql('imdb_database', con = engine, if_exists = 'replace', index = False)

df.to_csv('imdb_analysis', index = False)

# Connect to SQL Server
'''cnxn_str = ("Driver = {ODBC Driver 17 for SQL Server};"
            "Server = erinakim.database.windows.net;"
            "Database = erinaDB;"
            "Database_con = f'mssql://;"
            "Trusted_Connection=False;"
            "Encrypt=True;"
            "Integrated Security=False;"
            "UID=erinakim;"
            "PWD=1Ksy8327@!#;")

OR

server = 'erinakim.database.windows.net' 
database = 'erinaDB' 
username = 'erinakim' 
password = '1Ksy8327@!#'

cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};
                    SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password';)
cursor = cnxn.cursor()
'''
                      
# Create the engine
'''engine = create_engine(Database_IMDB)
pd.read_sql('df', engine)'''
