/*Q4) display the details of the movie with top 5 longest duration*/

movies = load 'IMDb Movies.csv' USING PigStorage(',') as (title:chararray, original_title:chararray, year:int, genre:chararray, duration:int, country:chararray, language:chararray, votes:int, users_review:int, critics_review:int);

A = order movies BY duration desc;
B = LIMIT A 5;
dump B;