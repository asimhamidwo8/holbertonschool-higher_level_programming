#!/usr/bin/env bash
# Run a suite of SQL commands to test the SQL_introduction scripts.
# Run this inside WSL in the SQL_introduction folder, e.g.:
#   cd ~/holbertonschool-higher_level_programming/SQL_introduction
#   bash run_sql_suite.sh

set -euo pipefail

if ! command -v mysql >/dev/null 2>&1; then
  echo "mysql client not found. Install it in WSL with: sudo apt update && sudo apt install -y default-mysql-client"
  exit 2
fi

echo '--- SHOW DATABASES (before) ---'
mysql -e 'SHOW DATABASES;'

echo
echo '--- Run create DB script (1-create_database_if_missing.sql) ---'
mysql < 1-create_database_if_missing.sql || true

echo
echo '--- SHOW DATABASES (after create) ---'
mysql -e 'SHOW DATABASES;'

echo
echo '--- Create table first_table in hbtn_0c_0 (4-first_table.sql) ---'
mysql hbtn_0c_0 < 4-first_table.sql || true

echo
echo '--- SHOW TABLES in hbtn_0c_0 ---'
mysql hbtn_0c_0 -e 'SHOW TABLES;'

echo
echo '--- SHOW CREATE TABLE first_table ---'
mysql hbtn_0c_0 -e 'SHOW CREATE TABLE first_table;'

echo
echo '--- Insert one row into first_table (7-insert_value.sql) ---'
mysql hbtn_0c_0 < 7-insert_value.sql || true

echo
echo '--- List values in first_table (6-list_values.sql) ---'
mysql hbtn_0c_0 -e "SELECT * FROM first_table;"

echo
echo '--- Insert same row again (7-insert_value.sql) to show repeated inserts ---'
mysql hbtn_0c_0 < 7-insert_value.sql || true

echo
echo '--- List values in first_table (after second insert) ---'
mysql hbtn_0c_0 -e "SELECT * FROM first_table;"

echo
echo '--- Count id=89 (8-count_89.sql) ---'
mysql hbtn_0c_0 -e "SELECT COUNT(*) FROM first_table WHERE id = 89;"

echo
echo '--- Create second_table and insert rows (9-full_creation.sql) ---'
mysql hbtn_0c_0 < 9-full_creation.sql || true

echo
echo '--- List second_table ordered by score desc (10-top_score.sql) ---'
mysql hbtn_0c_0 -e "SELECT score, name FROM second_table ORDER BY score DESC;"

echo
echo '--- List second_table where score >= 10 (11-best_score.sql) ---'
mysql hbtn_0c_0 -e "SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;"

echo
echo '--- Update Bob to score 10 (12-no_cheating.sql) ---'
mysql hbtn_0c_0 < 12-no_cheating.sql || true

echo
echo '--- List second_table after update ---'
mysql hbtn_0c_0 -e "SELECT score, name FROM second_table ORDER BY score DESC;"

echo
echo '--- Delete records with score <= 5 (13-change_class.sql) ---'
mysql hbtn_0c_0 < 13-change_class.sql || true

echo
echo '--- List second_table after deletions ---'
mysql hbtn_0c_0 -e "SELECT score, name FROM second_table ORDER BY score DESC;"

echo
echo '--- Average score (14-average.sql) ---'
mysql hbtn_0c_0 -e "SELECT AVG(score) AS average FROM second_table;"

echo
echo '--- Group by score with counts (15-groups.sql) ---'
mysql hbtn_0c_0 -e "SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;"

echo
echo '--- List where name not empty ordered (16-no_link.sql) ---'
mysql hbtn_0c_0 -e "SELECT score, name FROM second_table WHERE name IS NOT NULL AND name <> '' ORDER BY score DESC;"

echo
echo '--- Drop database (2-remove_database.sql) ---'
mysql < 2-remove_database.sql || true

echo
echo '--- SHOW DATABASES (after drop) ---'
mysql -e 'SHOW DATABASES;'

echo
echo '--- Test suite finished ---'
