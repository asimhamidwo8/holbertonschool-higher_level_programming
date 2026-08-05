-- Group by score and count as number ordered by number desc
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
