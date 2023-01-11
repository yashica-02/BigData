dvds = LOAD 'dividends.txt' USING PigStorage(' ') as (exchange: chararray, symbol:chararray, date:chararray, dividend:float);

grp = GROUP dvds by symbol;
avg = foreach grp generate group , AVG(dvds.dividend);

DUMP avg;