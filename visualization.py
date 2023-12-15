import psycopg2 
import matplotlib.pyplot as plt

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

labels_a, values_a= zip(*results_a)
labels_b, values_b= zip(*results_b)
labels_c, values_c= zip(*results_c)


fig, ax = plt.subplots(1, 3, figsize = (15, 5))
ax[0].bar(labels_a, values_a, color = 'green')
ax[0].set_title('Кількість манги для кожного жанру')
ax[0].set_xlabel('Жанр')
ax[0].set_ylabel('Кількість')

ax[1].pie(values_b, labels=labels_b, autopct='%1.1f%%')
ax[1].set_title('Кількість манги за кожним статусом')

ax[2].bar(labels_c, values_c, color = 'red')
ax[2].set_xlabel('Статус')
ax[2].set_ylabel('Кількість розділів')
ax[2].set_title('Залежність кількості розділів від завершеності манги')

plt.tight_layout()
plt.show()