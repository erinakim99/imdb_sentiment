# IMDB 50K Review Sentiment Analysis
Finding the linguistic features on IMDB Review sentiments

## Pre-analysis
- Downloaded 50,000 IMDB Reviews with filtered sentiments
>https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
- Downloaded positive/negative adjective lists
>https://gist.github.com/mkulakowski2/4289437

## Building a DataFrame
- Tokenized each review with nltk library

`token_list = imdb['review'].map(tokenizer.tokenize)`

- Created a DataFrame to arrange the information

`df = pd.DataFrame()`

- Counted number of words & first pronouns and saved as df columns

`df['Number of Words'] = count_list`
`for idx in token_list:`
`    count_list.append(len(idx))`

`pronoun = ['i','my', 'me', 'mine','myself']`
`df['Number of First Pronoun'] = pronoun_match`
`for token in idx:`
`        if token.lower() in pronoun:`
`            pronoun_count += 1`
`pronoun_match.append(pronoun_count)`

- Analyzed the word tone using the positive / negative list
`if ps_count > ng_count:`
`        tone.append("positive")`
`    elif ps_count < ng_count:`
`        tone.append("negative")`
`    else:`
`        tone.append("neutral")`

- Converted the DataFrame to SQL DataBase after the analysis

`engine = create_engine('sqlite:///C:\\Erina\\SQL Practice\\imdb_database.db?charset=utf8', echo = False)`

`df.to_sql('imdb_database', con = engine, if_exists = 'replace', index = False)`

## Analyzing with SQL
- Compared 3 following factors for each sentiment (positive/negative)
1) Average Number of words

`SELECT AVG("Number of Words") FROM imdb_database WHERE [Rating] = 'positive';`

`SELECT AVG("Number of Words") FROM imdb_database WHERE [Rating] = 'negative';`

2) Average Number of First Personal Pronouns

`SELECT AVG("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'positive';`

`SELECT AVG("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'negative';`

3) Total Number of First Personal Pronouns

`SELECT SUM("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'positive';`

`SELECT SUM("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'negative';`

- Counted the Matching Number of [Word Tone] with Actual Rating

`SELECT COUNT("Rating") FROM imdb_database WHERE [Rating] = [Word Tone];`
