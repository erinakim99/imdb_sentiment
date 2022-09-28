# IMDB 50K Review Sentiment Analysis
Finding the linguistic features on IMDB Review sentiments

## Pre-analysis
**Downloaded 50,000 IMDB Reviews with filtered sentiments**
>https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews<

**Downloaded positive/negative adjective lists**
>https://gist.github.com/mkulakowski2/4289437<

## Building a DataFrame
**1. Tokenized each review with nltk library**

- `token_list = imdb['review'].map(tokenizer.tokenize)`

**2. Created a DataFrame to arrange the information**

- `df = pd.DataFrame()`

**3. Counted number of words & first pronouns and saved as df columns**

- `df['Number of Words'] = count_list`

- `pronoun = ['i','my', 'me', 'mine','myself']`

- `df['Number of First Pronoun'] = pronoun_match`

>![image](https://user-images.githubusercontent.com/43493266/192659196-fc05f7c0-c486-4e0a-ae06-ab2baa64e63e.png)
![image](https://user-images.githubusercontent.com/43493266/192659381-6d272d06-04bb-47ca-afcc-c94b4dba7866.png)

**4. Analyzed the word tone using the positive / negative list**

>![image](https://user-images.githubusercontent.com/43493266/192659006-4b687753-2757-41de-aa24-82964df3914b.png)
![image](https://user-images.githubusercontent.com/43493266/192659125-eea721fd-59f1-494b-b505-e0de866112af.png)

**5. Converted the DataFrame to SQL DataBase after the analysis**

- `engine = create_engine('sqlite:///C:\\Erina\\SQL Practice\\imdb_database.db?charset=utf8', echo = False)`

- `df.to_sql('imdb_database', con = engine, if_exists = 'replace', index = False)`

## Analyzing with SQL
**1. Compared 3 following factors for each sentiment (positive/negative)**

*Average Number of words*

- `SELECT AVG("Number of Words") FROM imdb_database WHERE [Rating] = 'positive';`

- `SELECT AVG("Number of Words") FROM imdb_database WHERE [Rating] = 'negative';`

*Average Number of First Personal Pronouns*

- `SELECT AVG("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'positive';`

- `SELECT AVG("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'negative';`

*Total Number of First Personal Pronouns*

- `SELECT SUM("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'positive';`

- `SELECT SUM("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'negative';`

**2. Counted the Matching Number of [Word Tone] with Actual Rating**

- `SELECT COUNT("Rating") FROM imdb_database WHERE [Rating] = [Word Tone];`
