/*Q2) display the movie title from genre given by the user having 400+ votes, 8+ rating from user or from critics*/

--pig -x local -param “genre=” PigQ2.pig

movies = load 'IMDb Movies.csv' USING PigStorage(',') as (title:chararray, original_title:chararray, year:int, genre:chararray, duration:int, country:chararray, language:chararray, votes:int, users_review:int, critics_review:int);

A = filter movies by genre == '$genre' AND votes >400 AND (users_review>8 OR critics_review>8);
B = foreach A generate title;
dump B;