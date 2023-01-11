/*Q1) Display the longest duration of movies of each genre*/

movies = load 'IMDb Movies.csv' USING PigStorage(',') as (title:chararray, original_title:chararray, year:int, genre:chararray, duration:int, country:chararray, language:chararray, votes:int, users_review:int, critics_review:int);

A = foreach movies generate genre, duration;
B = Group A by genre;
C = foreach B {
    D = order A by duration desc;
    E = limit D 1;
    generate flatten(E);
}
dump C;