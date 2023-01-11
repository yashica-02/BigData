A = load '1.txt' using PigStorage (',') as (FName: chararray, LName: chararray, MobileNo: chararray, City: chararray, Profession: chararray);

B = foreach A generate FName, MobileNo, City;

dump A;

dump B;