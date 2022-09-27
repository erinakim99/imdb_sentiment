# imdb_sentiment
Finding the linguistic features on IMDB Review sentiments

## Pre-analysis
- Downloaded 50,000 IMDB Reviews with filtered sentiments: kaggle datasets download -d lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
- Downloaded positive/negative adjective lists
<script src="https://gist.github.com/mkulakowski2/4289437.js"></script>,
<script src="https://gist.github.com/mkulakowski2/4289441.js"></script>

## Building a DataFrame
- Tokenized each review with nltk library
`token_list = imdb['review'].map(tokenizer.tokenize)`
- Created a DataFrame to arrange the information
`df = pd.DataFrame()`
- Counted number of words & first pronouns and saved as df columns
`df['Number of Words'] = count_list
df['Number of First Pronoun'] = pronoun_match`
- Analyzed the word tone using the positive / negative list
`pronoun = ['i','my', 'me', 'mine','myself']`
- Converted the DataFrame to SQL DataBase after the analysis
`engine = create_engine('sqlite:///C:\\Erina\\SQL Practice\\imdb_database.db?charset=utf8', echo = False)
df.to_sql('imdb_database', con = engine, if_exists = 'replace', index = False)`

## Analyzing with SQL
- Compared 3 following factors for each sentiment (positive/negative)
# Average Number of words
`SELECT AVG("Number of Words") FROM imdb_database WHERE [Rating] = 'positive';
SELECT AVG("Number of Words") FROM imdb_database WHERE [Rating] = 'negative';`
# Average Number of First Personal Pronouns
`SELECT AVG("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'positive';
SELECT AVG("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'negative';`
# Total Number of First Personal Pronouns
`SELECT SUM("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'positive';
SELECT SUM("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'negative';`

- Counted the Matching Number of [Word Tone] with Actual Rating
`SELECT COUNT("Rating") FROM imdb_database WHERE [Rating] = [Word Tone];`
