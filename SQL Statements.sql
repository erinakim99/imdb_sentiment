1. Average Number of Words
SELECT AVG("Number of Words") FROM imdb_database WHERE [Rating] = 'positive';
SELECT AVG("Number of Words") FROM imdb_database WHERE [Rating] = 'negative';

2. Average Number of First Pronouns
SELECT AVG("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'positive';
SELECT AVG("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'negative';

3. Total Number of First Pronouns
SELECT SUM("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'positive';
SELECT SUM("Number of First Pronoun") FROM imdb_database WHERE [Rating] = 'negative';

4. Accuracy of Word Tone (Total Number of Matching columns)
SELECT COUNT("Rating") FROM imdb_database WHERE [Rating] = [Word Tone];