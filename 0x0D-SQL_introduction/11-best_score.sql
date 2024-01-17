-- lists all rows of second_table
-- from database hbtn_0c_0
-- ordered by score and score >= 10
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
