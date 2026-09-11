#!/usr/bin/python3
"""List all cities of a given state."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (sys.argv[4],)
    )

    cities = [city[0] for city in cursor.fetchall()]
    print(", ".join(cities))

    cursor.close()
    db.close()

