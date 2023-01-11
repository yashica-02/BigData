/*Q3) display the title of movies that start from "The" without it starting from 'The' and were made in 1914,1920,1921 and 1926*/

movies = load 'IMDb Movies.csv' USING PigStorage(',') as (title:chararray, original_title:chararray, year:int, genre:chararray, duration:int, country:chararray, language:chararray, votes:int, users_review:int, critics_review:int);

A = filter movies by STARTSWITH(title,'The') AND year IN(1914,1920,1921,1926);
B = foreach A generate REPLACE(title,'The ',''),genre;
dump B;