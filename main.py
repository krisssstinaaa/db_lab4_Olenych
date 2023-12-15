import psycopg2 
params = {
    'user': 'postgres',
    'password': '1111',
    'database': 'labs',
    'host': 'localhost',
    'port': '5432'
}

conn = psycopg2.connect(**params)
cur = conn.cursor()

query_a = """
    SELECT g.genre, COUNT(mg.manga_id) AS manga_count
    FROM genre g
    JOIN manga_genre mg ON g.genre_id = mg.genre_id
    GROUP BY g.genre;
"""

query_b = """
    SELECT s.status, COUNT(m.manga_id) AS manga_count
    FROM status s
    JOIN manga m ON s.status_id = m.status_id
    GROUP BY s.status;
"""

query_c = """
    SELECT s.status, AVG(m.chapters) AS avg_chapters
    FROM manga m
    JOIN status s ON m.status_id = s.status_id
    GROUP BY s.status;
"""
cur.execute(query_a)
results_a = cur.fetchall()

cur.execute(query_b)
results_b = cur.fetchall()

cur.execute(query_c)
results_c = cur.fetchall()

print("Query a:")

for row in results_a:
    print(row)

print("\nQuery b:")

for row in results_b:
    print(row)

print("\nQuery c:")

for row in results_c:
    print(row)

cur.close()
conn.close()